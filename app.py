import os
import requests
import streamlit as st
import pdfplumber



def main(file):
    with pdfplumber.open(file) as pdf:
        page = pdf.pages[0]
        text = page.extract_text(x_tolerance=2)
        return text




st.title("invoice processing")
file = st.file_uploader("choose a file to extract")
element = st.text_input("enter the parameter to extract")
if st.button('classify'):
        c = main(file)
        st.write(c)
for column in c.split('\n'):
    if column.startswith(element):
        word = column.split()[-1]

st.write("element:",word)







