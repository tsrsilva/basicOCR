import os
from jiwer import cer, wer

def get_clean_text(file_path):
    """Reads a file and removes headers/labels for a fair comparison."""
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Filter out 'IMAGE:' and 'Label X:' headers if they exist
    clean_lines = []
    for line in lines:
        if not line.startswith(("IMAGE:", "Label 1:", "Label 2:", "Label 3:")):
            clean_lines.append(line.strip())
        else:
            # If it has a header, just take the text after the colon
            if ":" in line:
                clean_lines.append(line.split(":", 1)[1].strip())
                
    return " ".join(clean_lines).strip()

def run_analysis(gt_folder, results_file):
    # 1. Get the OCR output for comparison
    # (For now, we'll assume the results_file matches your ground truth file)
    # In a professional setup, you'd parse label_results.txt to find the matching filename
    
    gt_file = os.path.join(gt_folder, "ufv-labecol-000097_l_1_high.txt")
    
    if not os.path.exists(gt_file):
        print(f"❌ Error: Could not find ground truth file at {gt_file}")
        return

    # Load and clean
    reference = get_clean_text(gt_file)
    # For a quick test, we will use the text you just pasted in the chat as 'hypothesis'
    hypothesis = "Brasil, Viçosa, MG Floresta Secundária I-1994 Sperber; Louzada & Lopes unique specimen identifier DO NOT REMOVE UFV-LABECOL-000097 Specimen photographed J. Chaul, 2015"

    # Calculate
    error_char = cer(reference, hypothesis)
    error_word = wer(reference, hypothesis)

    print(f"--- Accuracy Report ---")
    print(f"CER: {error_char:.2%} (Character-level accuracy: {1-error_char:.2%})")
    print(f"WER: {error_word:.2%} (Word-level accuracy: {1-error_word:.2%})")

if __name__ == "__main__":
    run_analysis('data/ground_truth', 'outputs/text/label_results.txt')