from tkinter import *
from tkinter import messagebox
def show():
    messagebox.showinfo("CDJ","BBACA Info")
def disp():
    messagebox.askquestion("Are you sure")
window=Tk()
window.geometry("500x200")
b1=Button(window,text="bca", command=show)
b2=Button(window,text="bcs",command=disp)
b1.pack()
b2.pack()
window.mainloop()
