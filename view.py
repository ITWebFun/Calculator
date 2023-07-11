from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Calculator')
root.geometry('470x630')
root.minsize(height=630, width=470)
root.maxsize(height=630, width=470)

label=Label(text='Calculator',font='Times 18 bold')
label.grid(row=0,column=0,columnspan=4, pady=5)

entry = Entry(textvariable='', font='Times 18 bold')
entry.grid(row=1,column=1,columnspan=2, pady=5)

def add_to_expression():
    return

btn_C = Button(text='C',font='Times 18 bold',height=3, width=6, command=add_to_expression)
btn_C.grid(row=2,column=0,pady=5, padx=5)

btn_divine = Button(text='/',font='Times 18 bold',height=3, width=6, command=add_to_expression)
btn_divine.grid(row=2,column=1,pady=5, padx=5)

btn_multiply = Button(text='*',font='Times 18 bold',height=3, width=6, command=add_to_expression)
btn_multiply.grid(row=2,column=2,pady=5, padx=5)

btn_substract = Button(text='-',font='Times 18 bold',height=3, width=6, command=add_to_expression)
btn_substract.grid(row=2,column=3,pady=5, padx=5)

btn_7 = Button(text='7',font='Times 18 bold',height=3, width=7, command=add_to_expression)
btn_7.grid(row=3,column=0,pady=5, padx=5)

btn_8 = Button(text='8',font='Times 18 bold',height=3, width=6, command=add_to_expression)
btn_8.grid(row=3,column=1,pady=5, padx=5)

btn_9 = Button(text='9',font='Times 18 bold',height=3, width=6, command=add_to_expression)
btn_9.grid(row=3,column=2,pady=5, padx=5)

btn_plus = Button(text='+',font='Times 18 bold',height=7, width=6, command=add_to_expression)
btn_plus.grid(row=3,column=3, rowspan=2,pady=5, padx=5)

btn_4 = Button(text='4',font='Times 18 bold',height=3, width=6, command=add_to_expression)
btn_4.grid(row=4,column=0,pady=5, padx=5)

btn_5 = Button(text='5',font='Times 18 bold',height=3, width=6, command=add_to_expression)
btn_5.grid(row=4,column=1,pady=5, padx=5)

btn_6 = Button(text='6',font='Times 18 bold',height=3, width=6, command=add_to_expression)
btn_6.grid(row=4,column=2,pady=5, padx=5)

btn_1 = Button(text='1',font='Times 18 bold',height=3, width=6, command=add_to_expression)
btn_1.grid(row=5,column=0,pady=5, padx=5)

btn_2 = Button(text='2',font='Times 18 bold',height=3, width=6, command=add_to_expression)
btn_2.grid(row=5,column=1,pady=5, padx=5)

btn_3 = Button(text='3',font='Times 18 bold',height=3, width=6, command=add_to_expression)
btn_3.grid(row=5,column=2,pady=5, padx=5)

btn_equals = Button(text='=',font='Times 18 bold',height=7, width=6, command=add_to_expression)
btn_equals.grid(row=5,column=3,rowspan=2,pady=5, padx=5)

btn_0 = Button(text='0',font='Times 18 bold',height=3, width=14, command=add_to_expression)
btn_0.grid(row=6,column=0,columnspan=2,pady=5, padx=5)

btn_point = Button(text='.',font='Times 18 bold',height=3, width=6, command=add_to_expression)
btn_point.grid(row=6,column=2,pady=5, padx=5)

root.mainloop()