# Q2. Write a python program to in the same interface as above and create a action when the button is click it will display some text.
import tkinter
from tkinter import *
import sys

root=Tk()
var=StringVar()
root.geometry("250x250")
def show():
    var.set("Hello wo")
b=Button(root,text="Hello",width=25,command=show)
b2=Button(root,text="exit",width=25, command=exit)
label=Label(root,textvariable=var,width=30)
b.pack()
b2.pack()
label.pack()
root.mainloop()
