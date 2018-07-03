#Q3. Create a frame using tkinter with any label text and two buttons.One to exit and other to change the label to some other text.
import tkinter
from tkinter import *
import sys
root=Tk()
root.geometry("250x250")
var=StringVar()
def show():
    var.set("hello py")
b1=Button(root,text="change label",command=show)
b2=Button(root,text="exit",command=exit)
var.set("hello world")
label=Label(root,textvariable=var,width=25)
f1=Frame(root)
b1.pack()
b2.pack()
label.pack()
root.mainloop()