import os
import requests

import pdfplumber
with pdfplumber.open('i2.pdf') as pdf:
    page = pdf.pages[0]
    text = page.extract_text(x_tolerance=2)

print(text)

for column in text.split('\n'):
    if column.startswith('Sub Total'):
        TOTAL = column.split()[-1]
print(TOTAL)