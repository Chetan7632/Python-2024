from tkinter import *
from tkinter import messagebox
def show():
    messagebox.showinfo("CDJ", "This is info massage")
    messagebox.showerror("CDJ", "This is error massage")
    messagebox.askokcancel("OK", "This is ok cancel")
    messagebox.askquestion("OK", "This is question")
    messagebox.showwarning("OK", "This is warnning")
    messagebox.askretrycancel("OK", "This is retry cancel")
    messagebox.askyesno("OK", "This is yes no")

window=Tk()
window.geometry("300x400")
b1=Button(window,text="submit",command=show)
b1.pack()
window.mainloop()
