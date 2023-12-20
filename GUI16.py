from tkinter import *
def add():
    a=v1.get()
    b=v2.get()
    a=int(a)
    b=int(b)
    c=a+b
    v3.set(c)
def  sub():
    a=int(v1.get())
    b=int(v2.get())
    c=a-b
    v3.set(c)
window=Tk()
window.geometry("300x400")
v1=StringVar()
v2=StringVar()
v3=StringVar()

l1=Label(window,text="Enter No1:")
l2=Label(window,text="Enter No2:")
l3=Label(window,text="Result:")
t1=Entry(window,textvariable=v1)
t2=Entry(window,textvariable=v2)
t3=Entry(window,textvariable=v3)

b1=Button(window,text="Add",command=add)
b2=Button(window,text="Sub",command=sub)

l1.grid(row=0,column=0)
t1.grid(row=0,column=1)
l2.grid(row=1,column=0)
t2.grid(row=1,column=1)
l3.grid(row=2,column=0)
t3.grid(row=2,column=1)
b1.grid(row=3,column=0)
b2.grid(row=3,column=1)

window.mainloop()

