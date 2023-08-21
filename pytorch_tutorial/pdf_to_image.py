import os
import pdfplumber
import re

directory = r'C:\\Users\\Manju\\Desktop\\dd\\aa'


a = 'Quick Answer:'
b = 'Detailed Answer:'
c = 'Quick Check'





for filename in os.listdir(directory):
    if filename.endswith('.pdf'):
        fullpath = os.path.join(directory, filename)

        with pdfplumber.open(fullpath) as pdf:
            pages = pdf.pages
            for i,pg in enumerate(pages):
                if i > 21:
                    page_text = pg.extract_text()
                    page_text = page_text.split('\n')

                    
                    all_q = ''

                    for i in page_text:
                        text=i.encode('ascii', 'ignore')
                        text = text.decode('utf-8')


                        if text.startswith(' A.') or text.startswith(' B.') or text.startswith(' C.')  or text.startswith(' D.') :
                            pass
                        else:
                            
                            text = text.replace(a, '')
                            text = text.replace(b, '')
                            text = text.replace(c, '')


                            all_q += text+' '


                    all_q = re.sub(r'\d\d', '',all_q) 

                    

                    print(all_q)
                   