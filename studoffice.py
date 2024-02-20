
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
from pathlib import Path


pdf_dir = Path(r"C:/Users/User/Desktop/dev/studoffice_automation/pdf")
txt_dir = Path(r"C:/Users/User/Desktop/dev/studoffice_automation/txt")
pattern = r"\d\d\d/\d{5}"

if __name__ == "__main__":
    for pdf_path in pdf_dir.glob('*.pdf'):
        pages = convert_from_path(pdf_path, 300)
        print(f"pages={pages}")
        for pageNum,imgBlob in enumerate(pages):
            text = pytesseract.image_to_string(imgBlob)
            num = re.findall(pattern, text)
            print(f"num: {num}")
            # if len(num)==1:
            #     break

        os.rename(pdf_path, os.path.join(pdf_dir, f"{num[0].replace("/", "_")}.pdf"))
            # with open(f'{pdf_path}.txt', 'a', encoding="utf-8") as the_file:
            #     the_file.write(text)
