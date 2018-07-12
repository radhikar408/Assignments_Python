import tkinter
from tkinter import *
import pymysql
db=pymysql.connect('localhost','root','khushbukhushi','note')
# note =""
# insrt_text = None
def savenote():
    db = pymysql.connect('localhost', 'root', 'khushbukhushi', 'note')
    cursor = db.cursor()
    global note
    global s
    global n
    note = insrt_text.get('1.0', 'end')
    s=subj.get()
    n=na.get()
    print(note)
    print(s)
    print(n)
    qrl="insert into notes  values('" + s + "','" + n + "','" + note + "');"
    try:
        cursor.execute(qrl)
        db.commit()
    except:
        db.rollback()
    # cursor.execute('insert into notes(data) values(\'' +n+ "\')")

    # db.commit()
    # db.close()

def insrt():
    insrt_root=Tk()
    insrt_root.geometry("500x500")
    global insrt_text
    global subj
    global na
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
    can = Button(insrt_root, text='CANCEL',command=exit)
    can.place(x=300,y=450)

