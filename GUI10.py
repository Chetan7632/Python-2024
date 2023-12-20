+from tkinter import *
from tkinter import messagebox
def show():
    messagebox.showinfo("CDJ","BBACA Info")
window=Tk()
window.geometry("500x200")
a=IntVar()
l1=Label(window,text="Enter No:")
l1.pack()
t1=Entry(window)
t1.pack()

b1=Button(window,text="ok", command=show)
b1.pack()
window.mainloop()
