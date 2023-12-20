val1=""
ch=""
from tkinter import *

def one():
    a=v1.get()+"1"
    v1.set(a)
def two():
    a=v1.get()+"2"
    v1.set(a)
def three():
    a=v1.get()+"3"
    v1.set(a)
def four():
    a=v1.get()+"4"
    v1.set(a)
def five():
    a=v1.get()+"5"
    v1.set(a)
def six():
    a=v1.get()+"6"
    v1.set(a)
def seven():
    a=v1.get()+"7"
    v1.set(a)
def eight():
    a=v1.get()+"8"
    v1.set(a)
def nine():
    a=v1.get()+"9"
    v1.set(a)
def zero():
    a=v1.get()+"0"
    v1.set(a)
def add():
    val1=v1.get()
    v2.set(val1)
    v3.set("+")
    v1.set("")
def sub():
    val1=v1.get()
    v2.set(val1)
    v3.set("-")
    v1.set("")
def multi():
    val1=v1.get()
    v2.set(val1)
    v3.set("*")
    v1.set("")
def div():
    val1=v1.get()
    v2.set(val1)
    v3.set("/")
    v1.set("")
def equal():
    val2=int(v1.get())
    val1=int(v2.get())
    ch=v3.get()
    if ch=="+":
        res=val1+val2
        v1.set(res)
    elif ch=="-":
        res=val1-val2
        v1.set(res)
    elif ch=="*":
        res=val1*val2
        v1.set(res)
    elif ch=="/":
        res=val1/val2
        v1.set(res)
        

window=Tk()
v1=StringVar()
v2=StringVar()
v3=StringVar()
val2=StringVar()

t1=Entry(window,textvariable=v1)
t2=Entry(window,textvariable=v2)
t3=Entry(window,textvariable=v3)
b1=Button(window,text="1",command=one)
b2=Button(window,text="2",command=two)
b3=Button(window,text="3",command=three)
b4=Button(window,text="4",command=four)
b5=Button(window,text="5",command=five)
b6=Button(window,text="6",command=six)
b7=Button(window,text="7",command=seven)
b8=Button(window,text="8",command=eight)
b9=Button(window,text="9",command=nine)
b0=Button(window,text="0",command=zero)
badd=Button(window,text=" + ",command=add)
bsub=Button(window,text=" - ",command=sub)
bempt1=Button(window,text="  ")
bempt=Button(window,text="  ")
bmulti=Button(window,text=" x ",command=multi)
bdiv=Button(window,text=" / ",command=div)
bequal=Button(window,text="=",command=equal)
t1.place(x=10,y=10)
b1.place(x=10,y=50)
b2.place(x=30,y=50)
b3.place(x=50,y=50)
badd.place(x=70,y=50)
b4.place(x=10,y=80)
b5.place(x=30,y=80)
b6.place(x=50,y=80)
bsub.place(x=70,y=80)
b7.place(x=10,y=110)
b8.place(x=30,y=110)
b9.place(x=50,y=110)
bmulti.place(x=70,y=110)
b0.place(x=30,y=140)
bempt.place(x=10,y=140)
bequal.place(x=50,y=140)
bdiv.place(x=70,y=140)
window.mainloop()
