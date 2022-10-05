from tkinter import *
from tkinter import messagebox
root= Tk()
root.title="message box"
# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno, askyesnocancel
def popup():
    response =messagebox.askyesno("This is my Popup!","Hello world")
    #Label(root,text=response).pack()
    if response==1:
         Label(root,text="you  clicked yes").pack()
    elif response==0:
         Label(root,text="you clicked no :((").pack()

Button(root, text="Popup", command=popup).pack()

root.mainloop()