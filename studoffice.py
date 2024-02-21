

import os
from PIL import Image
from pdf2image import convert_from_path
import pytesseract
import glob
import PyPDF2
from PyPDF2 import PdfFileReader
import re
from pathlib import Path
import lxml
from lxml.html import fromstring, tostring
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import FirefoxOptions



pdf_dir = Path(r"C:/Users/User/Desktop/dev/studoffice_automation/pdf")

pattern = r"\d\d\d/\d{5}"

if __name__ == "__main__":
    for pdf_path in pdf_dir.glob('*.pdf'):
        pages = convert_from_path(pdf_path, 300)
        for pageNum,imgBlob in enumerate(pages):
            text = pytesseract.image_to_string(imgBlob)
            num = re.findall(pattern, text)
        os.rename(pdf_path, os.path.join(pdf_dir, f"{num[0].replace("/", "_")}.pdf"))
