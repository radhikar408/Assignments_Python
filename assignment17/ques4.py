# Q4. Write a python program using tkinter interface to take an input in the GUI program and print it.
import _tkinter
from tkinter import *
root=Tk()
root.geometry("250x250")
def show():
    print(entry.get())
entry=Entry(root,width=25)
entry.pack()
b=Button(root,text="click",width=20,command=show)
b.pack()
root.mainloop()