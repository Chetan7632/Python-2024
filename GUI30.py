from tkinter import *
from tkinter import messagebox
def prime():
    flag=0
    n=int(t1.get())
    for i in range(2,n):
        if n%i==0:
            flag=1
            break
    if flag==0:
        messagebox.showinfo("Prime","Number is Prime")
    else:
        messagebox.showinfo("Prime","Number is not Prime")

def armstrong():
    n=int(t1.get())
    temp=n
    tot=0
    while temp>0:
        d=temp%10
        tot=tot+(d**3)
        temp=temp/10
    if n==tot:
        messagebox.showinfo("Armstrong","Number is Armstrong")
    else:
        messagebox.showinfo("Armstrong","Number is not Armstrong")

def perfect():
    n=int(t1.get())
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum=sum+i
    if sum==n:
        messagebox.showinfo("Perfect","Number is Perfect")
    else:
        messagebox.showinfo("Perfect","Number is not Perfect")

window=Tk()
l1=Label(window,text="Enter Number:")
t1=Entry(window)
r1=Radiobutton(window,text="Prime", value=1, command=prime)
r2=Radiobutton(window,text="Armstrong", value=2, command=armstrong)
r3=Radiobutton(window,text="Perfect", value=3, command=perfect)
l1.pack()
t1.pack()
r1.pack()
r2.pack()
r3.pack()
window.mainloop()
