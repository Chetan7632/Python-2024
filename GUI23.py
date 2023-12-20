from tkinter import *
def show():
    s=v1.get()
    s1=" "
    for ch in s:
        if ch==" ":
            s1=s1+'*'
        elif ch>='a' and ch<='z':
            s1=s1+ch.upper()
        elif ch>='A' and ch<='Z':
            s1=s1+ch.lower()
        elif ch>='0' and ch<='9':
            s1=s1+"?"
        else:
            s1=s1+ch
    v2.set(s1)
window=Tk()
window.geometry("300x400")
v1=StringVar()
v2=StringVar()
l1=Label(window,text="Enter String:")
l1.pack()
t1=Entry(window,textvariable=v1)
t1.pack()
l2=Label(window,text="Result:")
l2.pack()
t2=Entry(window,textvariable=v2)
t2.pack()
b1=Button(window,text="OK",command=show)
b1.pack()
window.mainloop()
