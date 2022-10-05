from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title('Learn about frames')
#root.iconbitmap("c:/GUI/images.png")

frame = LabelFrame(root, text="This is my frame", padx=5, pady=5)
frame.pack(padx=10,pady=10)

b= Button(frame, text="Don't Click Here")
b2= Button(frame, text="Definetly dont click here")
b.grid(row=0,column=0)
b2.grid(row=1,column=0)
root.mainloop()