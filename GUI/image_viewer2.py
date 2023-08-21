from tkinter import *
from tkinter import filedialog
import PIL
from PIL import ImageTk
from PIL import Image
import glob


root = Tk()
# root.title('Title')
# root.iconbitmap('tiktok_logo.png')

image_list = []


def browse_button():
	# Allow user to select a directory and store it in global var
	# called folder_path
	global folder_path
	global image_list	

	filename = filedialog.askdirectory()
	folder_path.set(filename)
	print(filename)
	root.title(filename)

	# my_label = Label(image=image)
	# my_label.grid(row=0, column=0, columnspan=3)


	folder = filename


	res = [i for i in glob.glob(folder+'/*jpg')]



	count = 0
	for img in res:

		count += 1
		image = img

		image = ImageTk.PhotoImage(Image.open(img).resize((700,500),Image.ANTIALIAS))
		image_list.append(image)




folder_path = StringVar()
lbl1 = Label(master=root,textvariable=folder_path)
lbl1.grid(row=0, column=1)
button2 = Button(text="Browse", command=browse_button)
button2.grid(row=2, column=1)



# folder = '/home/manju/Desktop/PCB/test/' 


# res = [i for i in glob.glob(folder+'*jpg')]

# image_list = []


# count = 0
# for img in res:

# 	count += 1
# 	image = img

# 	image = ImageTk.PhotoImage(Image.open(img).resize((700,500),Image.ANTIALIAS))
# 	image_list.append(image)



# my_label = Label(image=image)
# my_label.grid(row=0, column=0, columnspan=3)
image = ImageTk.PhotoImage(Image.open(img).resize((700,500),Image.ANTIALIAS))

def forward(image_number):
	global my_label
	global button_forward
	global button_back

	my_label.grid_forget()
	
	# print(image_list[image_number-1])

	my_label = Label(image=image_list[image_number-1])
	# my_label.grid_forget()



	button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
	button_back = Button(root, text="<<", command=lambda: back(image_number-1))
	
	if image_number == len(image_list):
		button_forward = Button(root, text=">>", state=DISABLED)

	my_label.grid(row=0, column=0, columnspan=3)
	button_back.grid(row=1, column=0)
	button_forward.grid(row=1, column=2)

def back(image_number):
	global my_label
	global button_forward
	global button_back

	my_label.grid_forget()
	my_label = Label(image=image_list[image_number-1])
	button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
	button_back = Button(root, text="<<", command=lambda: back(image_number-1))

	if image_number == 1:
		button_back = Button(root, text="<<", state=DISABLED)

	my_label.grid(row=0, column=0, columnspan=3)
	button_back.grid(row=1, column=0)
	button_forward.grid(row=1, column=2)






button_back = Button(root, text="<<", command=back, state=DISABLED)
button_exit = Button(root, text="Exit Program", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))


button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

# lle00070 

root.mainloop()