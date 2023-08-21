from tkinter import *
import PIL
from PIL import ImageTk
from PIL import Image
from tkinter import messagebox
from tkinter import simpledialog

import glob


root = Tk()
root.title('messagebox')


def popup():

	USER_INP = simpledialog.askstring(title="Create class name",
                                  prompt="")
                                  	
	print(USER_INP)
	

btn1 = Button(root,text = "Button", command=popup)
btn1.pack()

root.mainloop()


