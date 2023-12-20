from tkinter import *
from tkinter import messagebox
def show():
    messagebox.showinfo("CDJ","BBACA Info")
def disp():
    messagebox.askokcancel("Redirect","Redirecting you to www.javascript.com")
window=Tk()
window.geometry("500x200")
b1=Button(window,text="bca", command=show)
b2=Button(window,text="JavaScript",command=disp)
b1.pack()
b2.pack()
window.mainloop()
