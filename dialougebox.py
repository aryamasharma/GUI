from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root= Tk()
root.title("learn dialouge box")

def open():
    root.filename = filedialog.askopenfilename(initialdir="/gui", title="Select a File",filetypes=(("png files","*.png"),("all files","*.*")))
    my_label= Label(root, text=root.filename).pack()
    global my_image
    my_image= ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label= Label(image=my_image).pack()

my_button = Button(root, text="Open file", command= open)
root.mainloop()
