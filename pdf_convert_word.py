#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import pdf2docx

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: " + sys.argv[0] + " <PDF-file> <output-folder>")
        sys.exit(0)

    pdf_file = sys.argv[1]
    output_folder = sys.argv[2]
    
    docx_file = os.path.join(output_folder, os.path.splitext(os.path.basename(pdf_file))[0] + '.docx')
    converter = pdf2docx.Converter(pdf_file)
    converter.convert(docx_file, start=0, end=None)
    converter.close()
