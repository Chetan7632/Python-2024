from tkinter import *
def show():
    window.configure(bg="red")
def show1():
    window.configure(bg="yellow")
def show2():
    window.configure(bg="pink")
window=Tk()
window.geometry("300x400")
b1=Button(window,text="RED", command=show)
b2=Button(window,text="YELLOW", command=show1)
b3=Button(window,text="PINK", command=show2)
b1.pack()
b2.pack()
b3.pack()
window.mainloop()
