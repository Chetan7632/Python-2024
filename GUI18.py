from tkinter import *
window=Tk()
window.geometry("300x400")
c1=Checkbutton(window,text="Java")
c2=Checkbutton(window,text="Python")
c3=Checkbutton(window,text="OOSE")

r1=Radiobutton(window,text="Male",value=1)
r2=Radiobutton(window,text="FeMale",value=2)
r1.place(x=10,y=100)
r2.place(x=100,y=100)

lst=Listbox(window,height=5)
lst.insert(0,"FY")
lst.insert(1,"SY")
lst.insert(2,"TY")
lst.place(x=100,y=200)

window.mainloop()
