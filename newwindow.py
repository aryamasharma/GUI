from tkinter import *
root=Tk()
root.title("my window")

top= Toplevel()
top.title("new window")
label = Label(top, text="this is my new window")
label.pack()
root.mainloop()