import tkinter
from tkinter import *
import pymysql
from insert import *
from update import *
import sys



def del_note():
    del_root=Tk()
    del_root.geometry("500x500")
    insrt_text=Text(del_root,width='50',height='25')
    # insrt_text.place(x=50,y=40)
    # but=Button(del_root,text='DELETE')
    # but.place(x=400,y=450)
    # can = Button(del_root, text='CANCEL',command=exit)
    # can.place(x=300,y=450)

    lab = Label(del_root, text='subject')
    lab.place(x=30, y=40)
    subj = Entry(del_root, width='50')
    subj.place(x=100, y=40)
    lab2 = Label(del_root, text='name')
    lab2.place(x=30, y=80)
    na = Entry(del_root, width='50')
    na.place(x=100, y=80)
