#!/usr/bin/env python3
"""
Author : devoscientist <devoscientist@devo>
Date   : 2025-09-06
Purpose: Method-1: text reading from image using tesseract
"""

import argparse
import pytesseract
from PIL import Image


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Method-1: text reading from image using tesseract',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file_path',
                        metavar='str',
                        type=str,
                        help='path to image')

    parser.add_argument('-o',
                        '--outfile_path',
                        help='Path to output file',
                        metavar='str',
                        type=str,
                        default='./output/output.txt')

    return parser.parse_args()


# --------------------------------------------------
def extract_text(image_path):
    """

    :param image_path:
    :return: extracted text
    """
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)

    new_line_count = 0
    to_check = '\n'
    # for char in text:
    #     if char == to_check:
    #         new_line_count+=1
    modified_text = text.replace(to_check, '')
    return modified_text, new_line_count
# --------------------------------------------------

def main():
    """Make a jazz noise here"""
    args = get_args()
    image_path = args.file_path
    print(f'extracted text --> \n{extract_text(image_path)}')

# --------------------------------------------------
if __name__ == '__main__':
    main()
