from tkinter import *


root = Tk()


i = 0


def bt1():
	global i	
	i += 1
	label1 = Label(root,text = str(i),fg="green")
	label1.pack()


def bt2():
	global i
	i = i-1
	label2 = Label(root,text=str(i),fg="red")

	label2.pack()


button1 = Button(root,text="Button 1", fg="red", bg="gray", padx=20, pady=20 ,command=bt1)
button1.pack()

button2 = Button(root,text="Button 2", fg="red", bg="gray", padx=20, pady=20 ,command=bt2)
button2.pack()


root.mainloop()




