#Q1. Write a python program using tkinter interface to write Hello World and a exit button that closes the interface.
import tkinter
from tkinter import *
import sys
root=Tk()
def show():
    print("hello world")
b=Button(root,text="Hello",width=25,command=show)
b2=Button(root,text="exit",width=25, command=exit)

b.pack()
b2.pack()
root.mainloop()