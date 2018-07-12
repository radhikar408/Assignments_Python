import tkinter
from tkinter import *
import sys
import pymysql
import sys
root=Tk()
db=pymysql.connect('localhost','root','khushbukhushi','demo')
note =""
insrt_text = None
def savenote():
    db = pymysql.connect('localhost', 'root', 'khushbukhushi', 'versions')
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
    #mycursor.execute("""insert into notes values('$note','$subj','$na')""");

    #cursor.execute('insert into note values('"+note+"')")
    #cursor.execute("insert into notes values(\''+s+"\')")
    #cursor.execute("insert into notes  values('"+note+"','"+note+"','"+note+"');"
    qrl="insert into notes  values('" + note + "','" + s + "','" + n + "');"

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
    #insrt_text = Text(insrt_root, width='50', height='20')
    #note=insrt_text.get('1.0','end')
    #insrt_text.place(x=30, y=20)
    # but = Button(insrt_root, text='SAVE', command=savenote)
    # but.place(x=400, y=400)

    lab=Label(insrt_root,text='subject')
    lab.place(x=30,y=40)
    subj=Entry(insrt_root,width='50')
    subj.place(x=100, y=40)
    lab2 = Label(insrt_root, text='name')
    lab2.place(x=30, y=80)
    na=Entry(insrt_root,width='50')
    na.place(x=100,y=80)
    insrt_text=Text(insrt_root,width='50',height='20')
    #note=insrt_text.get('1.0','end')
    insrt_text.place(x=50,y=150)
    but=Button(insrt_root,text='SAVE',command=savenote)
    but.place(x=400,y=500)
    can = Button(insrt_root, text='CANCEL',command=exit)
    can.place(x=300,y=500)

root.geometry("500x500")
#root.resizable(False,False)
b1=Button(root,text="Add NOtes",width=21,command=insrt)
b2=Button(root,text="Hello",width=21)
b3=Button(root,text="Hello",width=21)
b1.place(x=5,y=10)
b2.place(x=150,y=10)
b3.place(x=330,y=10)
srclabel=Label(root,text="search",width='25')
entry=Entry(root,width=50)
searchbutt=Button(root,text="search",width='10')
# entry2=Entry(root,width=25)
# entry3=Entry(root,width=25)
entry.place(x=150,y=100)
srclabel.place(x=5,y=100)
searchbutt.place(x=470,y=95)
# entry2.place(x=50,y=6)
# entry3.place(x=50,y=90)
root.mainloop()