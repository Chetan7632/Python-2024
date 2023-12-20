from tkinter import *
def add():
    val=int(t1.get())
    for i in range(1,11):
        lst.insert(i,val*i)
window=Tk()
l1=Label(window,text="Enter Number:")
t1=Entry(window)
l2=Label(window,text="Table")
lst=Listbox(window)
b1=Button(window,text="Add", command=add)
l1.grid(row=0,column=0)
t1.grid(row=0,column=1)
l2.grid(row=1,column=0)
lst.grid(row=1,column=1)
b1.grid(row=2,column=0)
window.mainloop()

