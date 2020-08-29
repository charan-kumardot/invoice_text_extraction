# -*- coding: utf-8 -*-


import os

import requests
import pdfplumber
with pdfplumber.open('i2.pdf') as pdf:
    page = pdf.pages[0]
    text = page.extract_text(x_tolerance=2)
    print(text)

lines = text.split('\n')

print(lines)

import re

amt_re = re.compile(r'\.\d\d$')

subt = 0

for line in lines:
    if 'Sub Total' in line:
        break
    if amt_re.search(line):
        subt += float(line.split()[-1].replace(',', '').replace('$', ''))

print(subt)
print(lines)

