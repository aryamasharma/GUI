from tkinter import *
from PIL import ImageTk,Image


root= Tk()
root.title("Images")
#root.iconbitmap('images.png')

my_img1= ImageTk.PhotoImage(Image.open("images/me1.jpg"))
my_img2= ImageTk.PhotoImage(Image.open("images/me2.jpg"))
my_img3= ImageTk.PhotoImage(Image.open("images/me3.jpg"))
my_img4= ImageTk.PhotoImage(Image.open("images/me4.jpg"))

image_list=[my_img1, my_img2,my_img3,my_img4]

status= Label(root, text="Image 1 of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=W)

my_label = Label(image=my_img1, height = 360)
my_label.grid(row=0, column=0, columnspan=3)

def forward(image_number):
    global my_label
    global button_front
    global button_back
    my_label.grid_forget()
    status= Label(root, text="Image "+ str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=W)

    my_label= Label(image=image_list[image_number-1],height = 360)
    button_front= Button(root, text=">>", command= lambda: forward(image_number+1))
    button_back= Button(root, text="<<", command= lambda: backwards(image_number-1))
    if int(image_number) == 4:
        button_front= Button(root, text=">>", state= DISABLED)
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_front.grid(row=1 , column=2)
    status.grid(row=2, column=0, columnspan=3, sticky= W+E)


def backwards(image_number):
    global my_label
    global button_front
    global button_back
    global my_label
    global button_front
    global button_back
    my_label.grid_forget()
    status= Label(root, text="Image " +str(image_number)+ " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=W)

    my_label= Label(image=image_list[image_number-1], height = 360)
    button_front= Button(root, text=">>", command= lambda: forward(image_number+1))
    button_back= Button(root, text="<<", command= lambda: backwards(image_number-1))
    if int(image_number) == 1:
            button_back= Button(root, text="<<", state= DISABLED)
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_front.grid(row=1 , column=2)
    status.grid(row=2, column=0, columnspan=3, sticky= W+E)

button_back = Button(root, text="<<", command=backwards, state= DISABLED)
button_front= Button(root, text=">>",command=lambda: forward(2))
button_exit= Button(root, text="Exit Program", command = root.quit,)

button_back.grid(row=1, column=0)
button_front.grid(row=1 , column=2)
button_exit.grid(row=1 , column=1, pady=10)
status.grid(row=2, column=0, columnspan=3, sticky= W+E)
root.mainloop()