from ast import Lambda
from tkinter import *

root = Tk()
root.title("simple calculator")
e= Entry(root, width =35, border=5 )
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)




def button_click(number):
    #e.delete(0,END)
    current= e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))

def button_clear():
    e.delete(0,END)

def button_add():
    first_number = e.get()
    global f_num 
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0,END)
    
def button_substract():
    first_number = e.get()
    global f_num
    global math
    f_num = int(first_number)
    math = "substraction"
    e.delete(0,END)


def button_divide():
    global f_num 
    global math
    first_number = e.get()
    math="division"
    f_num = int(first_number)
    e.delete(0,END)


def button_multiply():
    global f_num
    global math
    first_number = e.get()
    math="multiply"
    f_num = int(first_number)
    e.delete(0,END)

def button_equal():
    second_number= 0
    second_number = e.get()
    e.delete(0,END)
    if math =="addition":
     e.insert(0,f_num+ int(second_number))
    elif math=="substraction":
        e.insert(0,f_num -int(second_number))
    elif math=="division":
        e.insert(0,f_num/int(second_number))
    elif math=="multiply":
        e.insert(0,f_num * int(second_number))
    



button_1= Button(root, text="1", padx=40,pady=20,command=lambda:button_click(1))
button_2= Button(root, text="2",padx=40,pady=20, command=lambda:button_click(2))
button_3= Button(root, text="3", padx=40,pady=20, command=lambda:button_click(3))
button_4= Button(root, text="4", padx=40,pady=20, command=lambda:button_click(4))
button_5= Button(root, text="5", padx=40,pady=20, command= lambda:button_click(5))
button_6= Button(root, text="6", padx=40,pady=20, command= lambda:button_click(6))
button_7= Button(root, text="7", padx=40,pady=20, command=lambda:button_click(7))
button_8= Button(root, text="8", padx=40,pady=20, command= lambda:button_click(8))
button_9= Button(root, text="9", padx=40,pady=20, command=lambda: button_click(9))
button_0= Button(root, text="0", padx=40,pady=20, command= lambda:button_click(0))
add_button = Button(root, text="+",padx=34,pady=20,command=button_add)
equal_button = Button(root, text="=", padx=91,pady=20,command=button_equal)
clear_button=Button(root, text="Clear", padx=80,pady=20,command= lambda:button_clear())

substract_button = Button(root, text="-",padx=40,pady=20,command=button_substract)
multiply_button = Button(root, text="*",padx=41,pady=20,command=button_multiply)
divide_button = Button(root, text="/",padx=40,pady=20,command=button_divide)
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)

add_button.grid(row=5, column=0)
equal_button.grid(row=5,column=1,columnspan=3)
clear_button.grid(row=4, column=1,columnspan=3)
substract_button.grid(row=6,column=0)
multiply_button.grid(row=6,column=1)
divide_button.grid(row=6,column=2)



root.mainloop()

