from tkinter import *
window=Tk()
Lb=Listbox(window)
Lb.insert(1, 'python')
Lb.insert(2, 'java')
Lb.insert(3, 'c++')
Lb.insert(4, 'any other')
Lb.pack()
window.mainloop()
