#Install dependencies
# glob
# openCV
# scikit-image
# easyocr
# pip install --force-reinstall -v "Pillow==9.5.0" ##Downgrade Pillow to 9.5.0

#Import libraries
import numpy as np
import cv2
import glob
from skimage.filters import gaussian
from skimage import img_as_ubyte

images_list = []
SIZE = 512

path = r'C:\Path_to_OCR\Input\*.*' #label input folder path

#First create a stack array of all images
for file in glob.glob(path):
    print(file)     #just stop here to see all file names printed
    img= cv2.imread(file, 0)  #now, we can read each file since we have the full path
    img = cv2.resize(img, (SIZE, SIZE))
    images_list.append(img)

images_list = np.array(images_list)

#Process each slice in the stack
img_number = 1
for image in range(images_list.shape[0]):
    input_img = images_list[image,:,:]  #Grey images. For color add another dim.
    smoothed_image = img_as_ubyte(gaussian(input_img, sigma=1, mode='constant', cval=0.0))
    (thresh, smoothed_image) = cv2.threshold(smoothed_image, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(smoothed_image, kernel, iterations=1)
    img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    cv2.imwrite(r'C:\Path_to_OCR\smoothed\smoothed_image{0}.jpg'.format(str(img_number)), smoothed_image)
    img_number +=1

    if not cv2.imwrite(r'C:\Path_to_OCR\smoothed\smoothed_image{0}.jpg'.format(str(img_number)), smoothed_image):
        raise Exception("Could not write image")


###########################################

import easyocr
import os

smooth = r'C:C:\Path_to_OCR\smoothed'

jpgnames = []
result=[]

for file in os.listdir(smooth):

    file_path = os.path.join(smooth, file)
    # just for the .jpg
    if file_path.endswith(".jpg"):
        jpgnames.append(file)
i=0
while i < len(jpgnames):
    reader = easyocr.Reader(['en', 'pt', 'es'], cudnn_benchmark=True)
    smooth_path=[smooth + "\\" + jpgnames[i]]
    print(smooth_path)
    result1 = reader.readtext_batched(smooth_path, n_width=800, n_height=600, detail=0, paragraph=True)
    print(result1)
    result.append(result1[0][0])

    i=i+1
    print(i)
print(result)

f = open(r'C:\Path_to_OCR\text\label_name.txt', "w", encoding="utf-8")  # .txt save path
for line in result:

    f.write(line + '\n')
f.close()
