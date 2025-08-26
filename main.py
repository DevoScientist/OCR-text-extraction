#!/usr/bin/env python3

import pytesseract
from PIL import Image
from utils.utils import write_to_file
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
    output_file_name = "tesseract.txt"
    output_path = f"./output/{output_file_name}"
    extracted_text = extract_text(image_path)
    print(f"extracted text: {extracted_text}")
    write_to_file(extracted_text, output_path)

if __name__ == "__main__":
    main()



