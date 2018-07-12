import tkinter
from tkinter import *
import pymysql
#from up import *
from insert import *
import update
from update import *
#from delete import *
import sys

global nameList
global listNotes
nameList=[]
db=pymysql.connect('localhost','root','khushbukhushi','note')
cursor = db.cursor()
def main():
    print("main")
    global listNotes
    root=Tk()

    root.geometry("600x600")
    #root.resizable(False,False)
    butttonAdNotes=Button(root,text="Add Notes",width=21,command=insrt)
    butttonUpdate=Button(root,text="UPDATE",width=21,command=update)
    buttonDelete=Button(root,text="DELETE",width=21, command=deleteNotes)
    butttonAdNotes.place(x=5,y=10)
    butttonUpdate.place(x=200,y=10)
    buttonDelete.place(x=400,y=10)
    labelSearch=Label(root,text="search",width='25')
    entry=Entry(root,width=50)
    buttonSearch=Button(root,text="search",width='10')
    entry.place(x=150,y=100)
    labelSearch.place(x=5,y=100)
    buttonSearch.place(x=470,y=95)
    listNotes = Listbox(root, width='80', height='24')
    listNotes.place(x=50, y=170)
    labelSaveNotes = Label(root, text='........YOUR SAVED NOTES........')
    labelSaveNotes.place(x=160, y=140)

    #print name of notes on screen
    cmd1="select name from notes"
    cursor.execute(cmd1)

    get_name = cursor.fetchall()
    for i in range(len(get_name)):
        nameList.append(get_name[i][0])
        listNotes.insert(END,get_name[i][0])
    root.mainloop()

def deleteNotes():
    print("deletenotes")
    global listNotes
    name=listNotes.get(ACTIVE)
    cmd="delete from notes where name=\'"+name+"\'"
    cursor.execute(cmd)
    cmd1 = "select name from notes"
    cursor.execute(cmd1)

    get_name = cursor.fetchall()
    listNotes.delete(1,END)
    for i in range(len(get_name)):
        nameList.append(get_name[i][0])
        listNotes.insert(END, get_name[i][0])
    db.commit()

main()