from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.title("my window")
btn=Button(root, text="Open second window", command=open()).pack()

def open():
 top= Toplevel()
 top.title("new window")
 label = Label(top, text="this is my new window")
 my_img=ImageTk.PhotoImage(Image.open("images.png"))
 my_label= Label(top,image=my_img).pack()
 label.pack()
root.mainloop()