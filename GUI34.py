from datetime import date
from tkinter import *
def show():
    s1=v1.get() 
    s2=s1.split("/")
    bd=date(int(s2[2]),int(s2[1]),int(s2[0]))
    cd=date.today()
    yy=cd.year-bd.year
    mm=cd.month-bd.month
    dd=cd.day-bd.day
    v2.set("Year="+str(yy)+"Month="+str(mm)+"Days="+str(dd))

window=Tk()
v1=StringVar
v2=StringVar
l1=Label(window,text="Enter dd/mm/yyyy format:")
t1=Entry(window,textvariable=v1)
l2=Label(window,text="Age:")
t2=Entry(window,textvariable=v2)
b1=Button(window,text="Generate",command=show)
l1.pack()
t1.pack()
l2.pack()
t2.pack()
b1.pack()
window.mainloop()
