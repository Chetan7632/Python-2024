import time
from tkinter import *
window=Tk()
window.title("Digital Clock")
window.geometry("300x300")
l1=Label(window,font=("Curier 30 bold"),bg="blue",fg="white",bd=30)
l1.grid(row=0,column=1)

def show():
    t=time.strftime("%H:%M:%S")
    l1.config(text=t)
    l1.after(50,show)
show()
window.mainloop()
