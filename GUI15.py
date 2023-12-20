from tkinter import *
from tkinter import messagebox
def show():
    messagebox.showinfo("CDJ","BBACA Info")
def disp():
    messagebox.askretrycancel("Application","Try again")
window=Tk()
window.geometry("500x200")
b1=Button(window,text="bca", command=show)
b2=Button(window,text="Application",command=disp)
b1.pack()
b2.pack()
window.mainloop()
