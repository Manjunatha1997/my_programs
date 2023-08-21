from tkinter import *
import PIL
from PIL import Image
from PIL import ImageTk
import glob


root = Tk()

image = PhotoImage(file="tiktok_logo.png")
root.iconphoto(False,image)

# my_img = ImageTk.PhotoImage(Image.open('tiktok_logo.png').resize((700,500),Image.ANTIALIAS))
# my_label = Label(image=my_img)
# my_label.pack()



folder = '/home/manju/Desktop/PCB/test/' 	


i = 0


def next():
	global i


	all_images = glob.glob(folder+'*.jpg')
	img = all_images[i]

	print(img)
	my_img = Image.open(img)
	my_img = my_img.resize((500,500),Image.ANTIALIAS)
	my_img = ImageTk.PhotoImage(my_img)
	# my_img = ImageTk.PhotoImage(Image.open(img).resize((700,500),Image.ANTIALIAS))
	my_label = Label(image=my_img)
	my_label.grid(row=0,column=0)


	# i += 1

button_next = Button(root,text="Next",command=next)
button_next.grid(row=1,column=0)


root.mainloop()





