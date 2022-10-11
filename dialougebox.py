from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root= Tk()
root.title("learn dialouge box")

root.filename = filedialog.askopenfilename(initialdir="/gui", title="Select a File",filetypes=(("png files","*.png"),("all files","*.*")))

root.mainloop()