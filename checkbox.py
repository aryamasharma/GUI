from tkinter import *
from PIL import ImageTk, Image

root= Tk()
root.title("checkboxes")
root.geometry("400x400")

def show():
    myLabel= Label(root, text=var.get()).pack()

var= StringVar()
c= Checkbutton(root,text="Check this box", variable= var, onvalue="On", offvalue="Off")
c.deselect()
c.pack()



myButton= Button(root, text="show selection", command= show).pack()
root.mainloop()