#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
from paddleocr import PaddleOCR, draw_ocr
from pdf2image import convert_from_path

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("Usage: " + sys.argv[0] + " <PDF-file>")
        sys.exit(0)
    
    pdf_file = sys.argv[1]
    
    ocr = PaddleOCR(use_angle_cls=True, lang='ch')
    pages = convert_from_path(pdf_file)
    for i, page in enumerate(pages):
        page_file = "%d.png" % i
        page.save(page_file, "png")
        result = ocr.ocr(page_file, cls=True)
        text_file = "%d.txt" % i
        with open(text_file, 'w') as f:
            for idx in range(len(result)):
                res = result[idx]
                for line in res:
                    f.write(line + os.linesep)
        
