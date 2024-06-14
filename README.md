# Python-Tools
Python Multitool Set


# Script PDF-Maker
PDF Maker from different images
There are several ways to set up the processing images and convert to PDF, such as image size alignment, image resizing, compression, etc.

## Usage

```
python script_pdfmaker.py -h
usage: script_pdfmaker.py [-h] [-i INPUT_DIR] [-o OUTPUT_PDFNAME] [-ext INPUT_FILE_EXTENSION [INPUT_FILE_EXTENSION ...]] [-sr RESIZE_RATIO] [-q QUALITY] [-opt] [-a]
example: python script_pdfmaker.py -ext JPG HEIC -sr 2.5 -q 40 -a

options:
  -h, --help            show this help message and exit
  -i INPUT_DIR, --input-dir INPUT_DIR
  -o OUTPUT_PDFNAME, --output-pdfname OUTPUT_PDFNAME
  -ext INPUT_FILE_EXTENSION [INPUT_FILE_EXTENSION ...], --input-file-extension INPUT_FILE_EXTENSION [INPUT_FILE_EXTENSION ...]
  -sr RESIZE_RATIO, --resize-ratio RESIZE_RATIO
  -q QUALITY, --quality QUALITY
  -opt, --optimize
  -a, --alignment

```

## Build exe file
```
make build
```