from tkinter import *
from PIL import ImageTk, Image

root= Tk()
root.title('dropdown menu')
root.geometry("400x400")

def show():
    myLabel= Label(root, text=clicked.get()).pack()

options = [
"Monday",
"Tuesday",
"Wednesday",
"Thursday",
"Friday",
"Saturday",
"Sunday",
]



clicked=StringVar()
clicked.set("Monday")
#drop = OptionsMenu(root,clicked, "Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
drop= OptionMenu(root, clicked, *options )
drop.pack()

myButton = Button(root, text="Show selection", command= show).pack()
root.mainloop()