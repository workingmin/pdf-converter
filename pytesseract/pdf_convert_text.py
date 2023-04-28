#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from pdf2image import convert_from_path
from PIL import Image
import pytesseract

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("Usage: " + sys.argv[0] + " <PDF-file>")
        sys.exit(0)
    
    pdf_file = sys.argv[1]

    pages = convert_from_path(pdf_file)
    for i, page in enumerate(pages):
        page_file = "%d.png" % i
        page.save(page_file, "png")
        image = Image.open(page_file)
        texts = pytesseract.image_to_string(image, lang='chi_sim')
        text_file = "%d.txt" % i
        with open(text_file, 'w') as f:
            f.write(''.join(texts))
