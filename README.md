![MIT license](https://img.shields.io/github/license/tsrsilva/basicOCR)

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

All dependencies can be installed via pip or conda.

<a name="configuration"></a>
## Configuration

Before starting the character recognition process, you will need to determine the
input and output directories in ocr_scr.py. Open the file with your favorite text
editor and call the input path (*i.e.* the directory that your files that are
going to be OCRed are located).

<a name="running"></a>
## Running

You can run the ocr script directly from your system's native shell:

````
python path/to/the/ocr_scr.py
````

Or you can run through the in-built console of your IDE of preference.

<a name="issues"></a>
### Issues

The most straightforwad mechanism for asking questions, reporting problems, or requesting additions to the script is the [issue tracker](https://github.com/tsrsilva/basicOCR/issues).
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTIxMjk5NDc4MzhdfQ==
-->