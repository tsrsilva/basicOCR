import cv2
import numpy as np
import easyocr
import os
import re

# SETUP
REQUIRED_FOLDERS = ['data/labels', 'outputs/text', 'data/ground_truth']
for folder in REQUIRED_FOLDERS:
    os.makedirs(folder, exist_ok=True)

# 1. INITIALIZE EASYOCR READER
reader = easyocr.Reader(['en', 'pt', 'es'], cudnn_benchmark=True)

# Define paths
input_path = 'data/labels/'
output_text_file = 'outputs/text/label_results.txt'

results_list = []

# 2. OPTIMIZATION FUNCTION
def optimize_image(img_gray):
    # 1. CLAHE (Contrast Limited Adaptive Histogram Equalization)
    # This "pops" the ink out from the background
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    contrasted = clahe.apply(img_gray)

    # 2. Adaptive Denoising 
    # Gaussian blur removes "salt and pepper" noise without blurring the letters
    smoothed = cv2.GaussianBlur(contrasted, (3, 3), 0)

    # 3. Adaptive Thresholding
    # This calculates the best cut-off for every pixel
    #thresh = cv2.adaptiveThreshold(
        #contrasted, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
        #cv2.THRESH_BINARY, 11, 2
    #)

    # 4.1. Morphological Closing
    # This fills in tiny gaps in the letters (like a faded 'o' or 'e')
    #kernel = np.ones((2, 2), np.uint8)
    #processed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

    # 4.2. Erosion: Makes black ink thicker in white backgrounds, which can help with very faint text
    #kernel = np.ones((2, 2), np.uint8)
    #eroded = cv2.erode(thresh, kernel, iterations=1)
    
    return smoothed

# 2.5. TEXT CLEANUP FUNCTION
def cleanup_text(text):
    # 1. Clean up "noisy" characters often found at line ends
    text = re.sub(r'[|\\@©®™]', '', text)

    # 2. Specific Biological/Location fixes
    corrections = {
        "REMGVE": "REMOVE",
        "Sparba": "Sperber",
        "Sperba": "Sperber",
        "JG 25": "J. Chaul, 2015",
        "Viçosa MG": "Viçosa, MG",
        "Secundária I-1994": "Secundária II - 1994"
    }
    
    for typo, correct in corrections.items():
        text = text.replace(typo, correct)
    
    # Regex: Fix UFV-LABECOL (Ensure it has 6 digits)
    # If it found 5 digits, it often missed a leading or trailing zero
    #text = re.sub(r'UFV-LABECOL-(\d{1,5})\b', lambda m: f"UFV-LABECOL-{m.group(1).zfill(6)}", text)
    
    return text.strip()

# 3. PROCESS IMAGES
for filename in os.listdir(input_path):
    if not filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        continue
        
    print(f"Processing: {filename}")
    full_path = os.path.join(input_path, filename)
    
    # Read image (Grayscale)
    img = cv2.imread(full_path, 0)
    
    # Upscale
    img = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
    
    # Smoothing logic (CLAHE + Gaussian Blur + Adaptive Thresholding)
    processed_img = optimize_image(img)

    # Run OCR
    ocr_result = reader.readtext(
        processed_img, 
        detail=0, 
        paragraph=False,
        mag_ratio=1.5,        # Magnification for detection
        #text_threshold=0.6,   # Adjust to be more or less lenient with faint ink
        #link_threshold=0.3,   # Help link letters that have gaps
        width_ths=0.5,        # Allow for wider gaps between words
        y_ths=0.07,            # Prevents merging lines that are too close vertically
        #add_margin=0.1,       # Add space around detected boxes
        decoder='greedy',     # 'greedy' is faster, 'beamsearch' is more accurate but slower, 
                              # requires GPU, and it's prone to hallucinations if the image is very noisy. 
                              # 'wordbeamsearch' is a good middle ground but also slower.
        #contrast_ths=0.1,     # Help detect low-contrast text
        #adjust_contrast=0.7   # Adjust contrast for better detection of faint text
    )
    
    print(f"Detected lines: {ocr_result}")

    #if ocr_result:
        # Check if it's a list; if so, add the items. If it's a string, wrap it in a list.
        #if isinstance(ocr_result, list):
            #results_list.extend(ocr_result)
        #else:
            #results_list.append(ocr_result)
    if ocr_result and len(ocr_result) >= 3: # Ensure we have at least some lines
        # 1. Clean up individual lines
        cleaned_lines = [cleanup_text(line) for line in ocr_result]

        print(f"Total lines found: {len(cleaned_lines)}")
        
        # 2. SAFE Grouping Logic
        # Instead of hard-coding 0:4, 4:7, etc., let's split the list into 3 chunks
        # This way, even if it finds 12 lines, it divides them logically.
        n = len(cleaned_lines)
        label1 = " ".join(cleaned_lines[0 : n//3])
        label2 = " ".join(cleaned_lines[n//3 : 2*n//3])
        label3 = " ".join(cleaned_lines[2*n//3 : ])
        
        results_list.append(f"IMAGE: {filename}")
        results_list.append(f"Label 1: {label1}")
        results_list.append(f"Label 2: {label2}")
        results_list.append(f"Label 3: {label3}\n")
    elif ocr_result:
        # If it found text but not enough to split into 3 labels
        results_list.append(f"IMAGE: {filename} (Partial Detect)")
        results_list.append(" ".join([cleanup_text(l) for l in ocr_result]) + "\n")
    else:
        results_list.append(f"--- No text detected in {filename} ---")

# 4. SAVE RESULTS
with open(output_text_file, "w", encoding="utf-8") as f:
    for line in results_list:
        f.write(line + '\n')

print("✅ Finished! Results saved to:", output_text_file)