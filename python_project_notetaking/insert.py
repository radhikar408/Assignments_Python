import tkinter
from tkinter import *
import pymysql
db=pymysql.connect('localhost','root','khushbukhushi','note')

textBox = None
cursor = db.cursor()
global note
global subject
global n
global insrt_text


def savenote():
    note = insrt_text.get('1.0', 'end')
    subject=subj.get()
    n=na.get()
    qrl="insert into notes  values('" + subject + "','" + n + "','" + note + "');"
    try:
        cursor.execute(qrl)
        db.commit()
    except:
        db.rollback()

def insrt():
    insrt_root=Tk()
    insrt_root.geometry("500x500")
    global textBox
    global subj
    global na
    global insrt_text
    lab=Label(insrt_root,text='subject')
    lab.place(x=30,y=40)
    subj=Entry(insrt_root,width='50')
    subj.place(x=100, y=40)
    lab2 = Label(insrt_root, text='name')
    lab2.place(x=30, y=80)
    na=Entry(insrt_root,width='50')
    na.place(x=100,y=80)
    insrt_text=Text(insrt_root,width='50',height='15')
    insrt_text.place(x=50,y=150)
    but=Button(insrt_root,text='SAVE',command=savenote)
    but.place(x=400,y=450)
    can = Button(insrt_root, text='CANCEL')
    can.place(x=300,y=450)

