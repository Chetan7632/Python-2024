from tkinter import *
def show1():
    l1.config(font=("Arial",30))
def show2():
    l1.config(font=("Gigi",15))
window=Tk()
l1=Label(window,text="CDJ BBACA")
c1=Checkbutton(window,text="Arial",command=show1)
c2=Checkbutton(window,text="Gigi",command=show2)
l1.pack()
c1.pack()
c2.pack()
window.mainloop()
