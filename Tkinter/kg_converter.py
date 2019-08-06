from tkinter import *

window = Tk()

def conversor():
    gramas=float(e2_value.get())*1000
    pounds=float(e2_value.get())*2.20462
    ounces=float(e2_value.get())*35.274
    t1.delete(1.0, END)
    t2.delete(1.0, END)
    t3.delete(1.1, END)
    t1.insert(END, gramas)
    t2.insert(END, pounds)
    t3.insert(END, ounces)


e1=Label(window, text="kg")
e1.grid(row=0, column=0)

e2_value=StringVar()
e2=Entry(window, textvariable=e2_value)
e2.grid(row=0, column=1)

b1=Button(window, text="Converter", command=conversor)
b1.grid(row=0, column=2)

l1=Label(window, text="Gramas")
l1.grid(row=1, column=0)

l2=Label(window, text="Pounds")
l2.grid(row=1, column=1)

l3=Label(window, text="Ounces")
l3.grid(row=1, column=2)

t1=Text(window, height=1,width=20)
t1.grid(row=2, column=0)

t2=Text(window, height=1, width=20)
t2.grid(row=2, column=1)

t3=Text(window, height=1, width=20)
t3.grid(row=2,column=2)

window.mainloop()
