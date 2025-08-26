#!/usr/bin/env python3

import pytesseract
from PIL import Image

#Method -1 : not good for catching letter "I" in the test image.
def extract_text(image_path):
    """
    #to use this function : Tesseract OCR engine should be installed first
    I am using Fedora so for me this is: sudo dnf install tesseract
    :param image_path:
    :return: text extracted from image
    """
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image,lang='eng')
    return text

def main():
    image_path = "./assets/ocr-test-01.jpeg"
    extracted_text = extract_text(image_path)
    print(f"extracted text: {extracted_text}")

if __name__ == "__main__":
    main()



