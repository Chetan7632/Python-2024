import tkinter
window=tkinter.Tk()
l1=tkinter.Label(window,text="Enter No 1:")
l1.pack()
t1=tkinter.Entry(window)
t1.pack()
l2=tkinter.Label(window,text="Enter No 2:")
l2.pack()
t2=tkinter.Entry(window)
t2.pack()
b1=tkinter.Button(window,text="Add")
b1.pack()
window.mainloop()
