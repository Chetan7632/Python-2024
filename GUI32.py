import random
import string
from tkinter import *
def show():
    s=String.ascii_letters+String.digits
    p=random.choices(s,k=10)
    v1.set(p)
window=Tk()
l1=Label(window,text="passward")
t1=Entry(window, textvariable=v1)
b1=Button(window,text="Generate",command=show)
l1.pack()
t1.pack()
b1.pack()
window.mainloop()
