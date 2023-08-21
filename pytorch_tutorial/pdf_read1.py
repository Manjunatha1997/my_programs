import PyPDF2
from matplotlib.pyplot import text
import pandas as pd
import re


pdfFileObj = open(r'C:\\Users\\Manju\\Desktop\\dd\\Nclex-RN practice questions ( PDFDrive ).pdf','rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pages = pdfReader.numPages




qs = []
ops = []
answers = []

a = 'Practice Exam 1 and Rationales7'
b = '6Chapter 1'


for i in range(22,pages-1):

        pageObj = pdfReader.getPage(i)
        text = pageObj.extractText().split('A.')
        # text = text.split('\n')
        # text = text.replace(a,'')
        # text = text.replace(b,'')

        exp = '^(\d\d).+(A.)$'
        print(len(text))
        for i in text:
            i = i.replace(a,'')
            i = i.replace(b,'')
            print(i)


            input()

    

pdfFileObj.close()


