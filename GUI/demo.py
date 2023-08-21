from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import glob



gui = Tk()
gui.geometry("800x500")
gui.title("Lincode")

def getFolderPath():
    folder_selected = filedialog.askdirectory()
    folderPath.set(folder_selected)
    folder = folderPath.get()
    print("Doing stuff with folder", folder)

def doStuff():
    folder = folderPath.get()
    print("Doing stuff with folder", folder)



folderPath = StringVar()
a = Label(gui ,text="Enter Path")
a.grid(row=0,column = 0)
E = Entry(gui,textvariable=folderPath)
E.grid(row=0,column=1)
btnFind = ttk.Button(gui, text="Browse Folder",command=getFolderPath)
btnFind.grid(row=0,column=2)

c = ttk.Button(gui ,text="find", command=doStuff)
c.grid(row=4,column=0)




gui.mainloop()


Hi nikil,

I studied some basic features of tkinter like,
	grid system
	buttons
	input fields





