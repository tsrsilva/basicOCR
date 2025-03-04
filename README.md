[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# BasicOCR
An ongoing project to create a pipeline to optimize Optical Character Recognition (OCR) of specimen labels.
This is a work in progress.

## Table of Contents
  * [Dependencies](#dependencies)
  * [Configuration](#configuration)
  * [Running](#running)
  * [Issues](#issues)

<a name="dependencies"></a>
## Dependencies

To properly run this script, you will need to install three dependencies:

  * [Glob](https://docs.python.org/3/library/glob.html)
  * [OpenCV](https://docs.opencv.org/4.x/index.html)
  * [scikit-image](https://scikit-image.org/)
  * [EasyOCR](https://www.jaided.ai/easyocr/)
  * [Pillow 9.5.0v](https://pypi.org/project/pillow/9.5.0/)

All dependencies can be installed via pip or conda. EasyOCR works best if you have a CUDA-compatible GPU. 
For Windows, you may need to install pytorch manually. Please follow the instructions from the [Pytorch website](https://pytorch.org/get-started/locally/). 
Make sure to select the right CUDA version you have. If you intend to run on CPU mode only, select CUDA = None.

<a name="configuration"></a>
## Configuration

Before starting the character recognition process, you will need to determine the
input directory in ocr_scr.py. Open the file with your favorite text
editor and call the input path (*i.e.* the directory where your files that will be OCRed are located).
Image preprocessing runs through scikit-image (a.k.a. skimage) and cv2, and requires some tinkering in the
ocr_scr.py if your results are suboptimal. You can modify it *ad libitum* by opening the ocr_scr.py file in your text editor 
of preference and changing the lines containing the ```smoothed_image``` arguments:

```
input_img = images_list[image,:,:]  #Grey images. For color add another dim.
    smoothed_image = img_as_ubyte(gaussian(input_img, sigma=1, mode='constant', cval=0.0))
    (thresh, smoothed_image) = cv2.threshold(smoothed_image, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    kernel = np.ones((1, 1), np.uint8)
    smoothed_image2 = cv2.dilate(smoothed_image, kernel, iterations=1)
    smoothed_image3 = cv2.morphologyEx(smoothed_image2, cv2.MORPH_CLOSE, kernel)
```


<a name="running"></a>
## Running

You can run the OCR script directly from your system's native shell:

````
python path/to/the/ocr_scr.py
````

Or you can run through the in-built console of your IDE of preference.

<a name="issues"></a>
### Issues

The most straightforward mechanism for asking questions, reporting problems, 
or requesting additions to the script is the [issue tracker](https://github.com/tsrsilva/basicOCR/issues).
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTIxMjk5NDc4MzhdfQ==
-->
