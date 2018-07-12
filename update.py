import tkinter
from tkinter import *
import pymysql
from insert import *
db=pymysql.connect('localhost','root','khushbukhushi','note')
note =""
insrt_text = None

global update_text
global subj
global na

def update():
    update_root=Tk()
    update_root.geometry("500x500")
    # global update_text
    # global subj
    # global na
    lab=Label(update_root,text='subject')
    lab.place(x=30,y=40)
    subj=Entry(update_root,width='50')
    subj.place(x=100, y=40)
    lab2 = Label(update_root, text='name')
    lab2.place(x=30, y=80)
    na=Entry(update_root,width='50')
    na.place(x=100,y=80)
    update_text=Text(update_root,width='50',height='15')
    update_text.place(x=50,y=150)
    but=Button(update_root,text='SAVE CHANGES',command=update_note)
    but.place(x=400,y=450)
    can = Button(update_root, text='CANCEL',command=exit)
    can.place(x=300,y=450)

def update_note():
   # db = pymysql.connect('localhost', 'root', 'khushbukhushi', 'note')
    cursor = db.cursor()
    global up_note
    global up_sub
    global up_nam
    up_note = update_text.get('1.0', 'end')
    up_sub=subj.get()
    up_nam=na.get()
    print(up_note)
    print(up_sub)
    print(up_nam)
   #  qr = "update table_name set col_name = value1 where col_name=value2 and col_name=value3"
   # if((up_sub==s)and(up_name==n)):
   #     qrl = "update update_val set data=up_note where sub= and na=
   #     try:
   #      cursor.execute(qrl)
   #      db.commit()
   #     except:
   #      db.rollback()
   #  else:
   #         exit()


