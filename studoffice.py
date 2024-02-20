
# !apt-get install ocrmypdf -q
# !pip install pdfplumber -q
# !pip install pytesseract
# !sudo apt install tesseract-ocr
# !sudo apt install tesseract-ocr-rus
# !sudo apt install imagemagick
# !pip install PyPDF2
# !pip install pdf2image
# !sudo apt-get install poppler-utils
# !pip install regex
# !pip install regex

import os
# import requests
from PIL import Image
from pdf2image import convert_from_path
import pytesseract
import glob
import PyPDF2
from PyPDF2 import PdfFileReader
import re

pdf = glob.glob(r"C:/Users/User/Desktop/dev/SCAN_20240208_164856784_007.pdf")

if __name__ == "__main__":
    for pdf_path in pdf:
        pages = convert_from_path(pdf_path, 500)

        for pageNum,imgBlob in enumerate(pages):
            # text = pytesseract.image_to_string(imgBlob,lang='rus')
            text = pytesseract.image_to_string(imgBlob)

            with open(f'{pdf_path}.txt', 'a', encoding="utf-8") as the_file:
                the_file.write(text)

    # with open(r"C:/Users/User/Documents/Scan/SCAN_20240208_164856784_007.pdf.txt", 'r') as fp:
    #     print(r"\d\d\d/\d{5}")