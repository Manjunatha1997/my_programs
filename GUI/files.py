from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import glob

root = Tk()



# filename = filedialog.askopenfilename(initialdir='/home/manju/Desktop/',title='select file',filetypes=(('png files','*.png'),('jpg files','*.jpg')))

# print(filename)

def open():
	folder_path = filedialog.askdirectory(initialdir='/home/manju/Downloads/dataset/test',title="select folder")
	res = glob.glob(folder_path+'/*.jpg')
	print(res)


btn = Button(root,text='Select folder',command=open)
btn.grid(row=0,column=1)






root.mainloop()