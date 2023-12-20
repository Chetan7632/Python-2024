from tkinter import *
from tkinter import *  
window=Tk()
window.geometry("500x200")
l1=Label(window,text="Enter no:")
t1=Entry(window)

l2=Label(window,text="Enter no:")
t2=Entry(window)

b1=Button(window,text="OK")
b2=Button(window,text="EXIT")

c1=Checkbutton(window,text="Java")
c2=Checkbutton(window,text="Python")

l1.grid(row=0,column=0)
t1.grid(row=0,column=1)
l2.grid(row=1,column=0)
t2.grid(row=1,column=1)
c1.grid(row=2,column=0)
c2.grid(row=3,column=0)

b1.grid(row=4,column=0)
b2.grid(row=4,column=1)
window.mainloop()
