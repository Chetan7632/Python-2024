from tkinter import *
def show():
    l1=["zero","one","two","three","four","five","six","seven","eight","nine"]
    s1=v1.get()
    s2=" "
    for d in s1:
        d=int(d)
        s2=s2+l1[d]
    v2.set(s2)
window=Tk()
window.geometry("300x400")
v1=StringVar()
v2=StringVar()
l1=Label(window,text="Enter Number:")
l1.pack()
t1=Entry(window,textvariable=v1)
t1.pack()
l2=Label(window,text="Result:")
l2.pack()
t2=Entry(window,textvariable=v2)
t2.pack()
b1=Button(window,text="OK", command=show)
b1.pack()
window.mainloop()
