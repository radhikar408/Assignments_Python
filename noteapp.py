import tkinter
from tkinter import *
import pymysql
from insert import *
from update import *
import sys

def main():

    print("cp4")
    root=Tk()
    db=pymysql.connect('localhost','root','khushbukhushi','note')
    cursor = db.cursor()
    root.geometry("600x600")
    #root.resizable(False,False)
    b1=Button(root,text="Add Notes",width=21,command=insrt)
    b2=Button(root,text="UPDATE",width=21,command=update)
    b3=Button(root,text="DELETE",width=21)
    b1.place(x=5,y=10)
    b2.place(x=160,y=10)
    b3.place(x=330,y=10)
    srclabel=Label(root,text="search",width='25')
    entry=Entry(root,width=50)
    searchbutt=Button(root,text="search",width='10')
    # entry2=Entry(root,width=25)
    # entry3=Entry(root,width=25)
    entry.place(x=150,y=100)
    srclabel.place(x=5,y=100)
    searchbutt.place(x=470,y=95)
    insrt_text = Listbox(root, width='62', height='24')
    insrt_text.place(x=50, y=170)
    lab2 = Label(root, text='........YOUR SAVED NOTES........')
    lab2.place(x=160, y=140)

    #print name of notes on screen
    cmd1="select name from notes"
    cursor.execute(cmd1)
    nameList=[]
    get_name = cursor.fetchall()
    for i in range(len(get_name)):
        nameList.append(get_name[i][0])
        insrt_text.insert(END,get_name[i][0])
    #update notes with button
    # print(get_name.get(ACTIVE))
    root.mainloop()
main()