from tkinter import *


root = Tk()


username = Entry(root,width=100)
username.pack()


def btn1():
	uname = Label(root, text = username.get())
	uname.pack()



button1 = Button(root,text="Button1",command=btn1)
button1.pack()




root.mainloop()




