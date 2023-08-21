import PyPDF2
from matplotlib.pyplot import text
import pandas as pd


pdfFileObj = open(r'C:\\Users\\Manju\\Desktop\\dd\\FREE NCLEX QUESTIONS (pdf) ( PDFDrive ).pdf','rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pages = pdfReader.numPages


qs = []
ops = []
answers = []

op1 = []
op2 = []
op3 = []
op4 = []


fw = open('questions_options.txt','w')

for i in range(2,pages-1):

        pageObj = pdfReader.getPage(i)
        if i %2 == 0:
            text = pageObj.extractText().split("\n")

            question = text[0]

            options = list(text[1:-1])

            opts = ''
            opt1 = []
            opt2 = []
            opt3 = []
            opt4 = []

            for opt in options:
                if not (opt.startswith('a.') or opt.startswith('b.') or opt.startswith('c.') or opt.startswith('d.')):
                    question += opt
                    df = pd.DataFrame({'Questions':question,'Option1':opt1,'Option2':opt2,'Option3':opt3,'Option4':opt4,'Answer':ans})
        # df.loc[len(df.index)] = [question,opt1,opt2,opt3,opt4,ans]

                else:
                    if opt.startswith('a.'):
                        opt1 = opt
                    elif opt.startswith('b.'):
                        opt2 = opt
                    elif opt.startswith('c.'):
                        opt3 = opt
                    elif opt.startswith('d.'):
                        opt4 = opt
                    
                    print(opt)
                    opts += opt
            ops.extend(opt1)
            ops.extend(opt2)
            ops.extend(opt3)
            ops.extend(opt4)

            

            fw.write(question+'\n')
            fw.write(opts+'\n')
            fw.write('*************************************\n')


            qs.append(question)
            ops.append(opts)
        else:
            print(i)
            ans = pageObj.extractText()
            fw.write(ans+'\n')
            fw.write('######################################\n')
            print(ans)
            answers.append(ans)
        # df = pd.DataFrame({'Questions':question,'Option1':opt1,'Option2':opt2,'Option3':opt3,'Option4':opt4,'Answer':ans})
        # df.loc[len(df.index)] = [question,opt1,opt2,opt3,opt4,ans]



        

pdfFileObj.close()


# df = pd.DataFrame({'Questions':qs,'Options':ops,'Answers':answers})
# df = pd.DataFrame({'Questions':qs,'Option1':ops,'Answers':answers})


# df.to_csv('file1.csv')




# df.loc[len(df.index)] = ['Amy', 89, 93]

