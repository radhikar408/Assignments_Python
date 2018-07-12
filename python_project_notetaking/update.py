import tkinter
from tkinter import *
import pymysql
from insert import *
# import noteapp
# from noteapp import *

db=pymysql.connect('localhost','root','khushbukhushi','note')
cursor = db.cursor()
insrt_text = None
global entryName
global buttonSearch
global update_text
global nameList
global name
nameList=[]



def update():
    update_root = Tk()
    update_root.geometry("500x500")

    global entryName
    global update_text
    labelName = Label(update_root, text='name')
    labelName.place(x=10, y=10)
    entryName=Entry(update_root,width=30)
    entryName.place(x=90, y=10)
    buttonSearch = Button(update_root, text="search", command=search)
    buttonSearch.place(x=300, y= 10)
    update_text=Text(update_root,width='50',height='25')
    update_text.place(x=50,y=40)
    buttonSave=Button(update_root,text='SAVE CHANGES',command=saveChanges)
    buttonSave.place(x=380,y=450)
    can = Button(update_root, text='CANCEL',command=exit)
    can.place(x=300,y=450)


def search():
    global name
    cmd1 = "select name from notes"
    cursor.execute(cmd1)
    get_name = cursor.fetchall()
    for i in range(len(get_name)):
        nameList.append(get_name[i][0])
    name=entryName.get()
    for names in nameList:
        if names==name:
            fetchdata(name)
            break

def fetchdata(names):
    global update_text
    cmd = "select data from notes where name= \'"+names+"\'"
    cursor.execute(cmd)
    textData = cursor.fetchall()
    update_text.delete("1.0","end")
    update_text.insert(INSERT, textData[0][0])

def saveChanges():
    global name
    global update_text
    textData = update_text.get('1.0', 'end')
    cmd1 = "update notes set data = Null where name= \'"+name+"\'"
    cursor.execute(cmd1)
    cmd="update notes set data=\'"+textData+"\' where name= \'"+name+"\'"
    cursor.execute(cmd)
    fetchdata(name)







# def up(event):
#     name = e.get()
#
#     for n in nameList:
#         if n == name:
#             search(n)
#             break
#
# root.bind("<return>",up)
#
# def search(name):
#     qr = "select data from notes where name = \'"+name+"\'"
#
# def update():
#     data = l.get()
#     x = e.get()
#     qr = "update notes set data = "+data+" where name = \'"+x+"\'"




