from tkinter import *
from tkinter import messagebox
def show():
    s1=t1.get()
    ch=t2.get()
    cnt=s1.count(ch)
    messagebox.showinfo("CDJ","Character count="+str(cnt))
window=Tk()
l1=Label(window,text="Enter String:")
t1=Entry(window)
l2=Label(window,text="Enter Character:")
t2=Entry(window)
b1=Button(window,text="Count Character", command=show)
l1.pack()
t1.pack()
l2.pack()
t2.pack()
b1.pack()
window.mainloop()
