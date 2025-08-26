#!/usr/bin/env python3
"""
Author : DevoScientist <devoscientist214@gmail.com>
Date   : 2025-08-27
Purpose: Neural Network version of extracting text from image
"""

import argparse
import easyocr
from utils.utils import write_to_file


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Neural Network version of extracting text from image',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # parser.add_argument('positional',
    #                     metavar='str',
    #                     help='A positional argument')

    parser.add_argument('-n',
                        '--filename',
                        help='give the filename',
                        metavar='str',
                        type=str,
                        default='output.txt')

    parser.add_argument('-i',
                        '--int',
                        help='A named integer argument',
                        metavar='int',
                        type=int,
                        default=0)

    parser.add_argument('-f',
                        '--file',
                        help='A readable file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default=None)

    parser.add_argument('-o',
                        '--on',
                        help='A boolean flag',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------

#Method-2 : using easyocr (A NN approach) still not able to
#           catch the letter "I" in the testing Image.
def extract_text(image_path):
    """
    using "easyocr" to extract text from image
    :param image_path:
    :return: text extracted from image
    """
    reader = easyocr.Reader(["en"])
    extracted_text = reader.readtext(image_path)

    text = "\n".join([det[1] for det in extracted_text])
    return text

def main():
    """Make a jazz noise here"""
    args = get_args()
    output_file_name = args.filename
    image_path = "./assets/ocr-test-01.jpeg"

    output_path = f"./output/{output_file_name}"
    extracted_text = extract_text(image_path)
    print(f"extracted text: {extracted_text}")
    write_to_file(extracted_text, output_path)


# --------------------------------------------------
if __name__ == '__main__':
    main()
