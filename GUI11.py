from tkinter import *
window=Tk()
window.geometry("500x200")
a=IntVar()
l1=Label(window,text="Enter No:")
l1.place(x=10,y=50)
t1=Entry(window)
t1.place(x=200,y=50)
window.mainloop()
