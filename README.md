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
Image preprocessing runs through scikit-image (a.k.a. skimage) and requires some tinkering in the
ocr_scr.py if your results are suboptimal. You can changeit *ad libitum* by opening the .py file in your IDE 
of preference and changing the following lines:

```
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
