from tkinter import *

root = Tk()
e= Entry(root,bg="black",fg="white",width=50,borderwidth=5)
e.pack()
e.get()
e.insert(0, "Enter Your Name : ")

def myClick():
  hello= "Hello " + e.get()
  myLabel= Label(root, text=hello)
  myLabel.pack()


myButton= Button(root,text="Enter",command=myClick, fg="blue",bg="cadetblue")
myButton.pack()
root.mainloop()

