#Ques1--
import tkinter
from tkinter import *
d={"Rdhika":1234567892,"jyoi":234567890,"khush":123456884,"aanchal":55667788,"rakul":9578686,"nihal":8957474785,"rahul":9578686,"avi":8957474785,"raman":9578686,"rajat":8957474785,"Radhi":1234567892,"jyot":234567890,"khushi":123456884,"Radhika":1234567892,"jyoti":234567890,"khushi":123456884}
root=Tk()
#root.resizable(False,False)
root.geometry("250x250")
root.minsize(50,50)
sc=Scrollbar(root)
sc.pack(side=RIGHT,fill=Y)
mylist=Listbox(root,yscrollcommand=sc.set)
for i in d:
    mylist.insert(END,i)
mylist.pack(fill=BOTH)
Scrollbar(mylist,orient="vertical")
sc.config(command=mylist.yview)
root.mainloop()

#Q2. In the same tkinter file as created above, create a function to insert items into the dictionary.
# import tkinter
# from tkinter import *
# d={"Radhika":1234567892,"jyoti":234567890,"khushi":123456884,"aanchal":55667788,"rahul":9578686,"nihal":8957474785}
# root=Tk()
# def show():
#     k=entry1.get()
#     v=entry2.get()
#     d[k]=v
#     mylist.insert(END,k)
#
# entry2=Entry(root)
# entry1=Entry(root)
# entry1.pack()
# entry2.pack()
#
# b=Button(root,text="Insert",command=show)
# b.pack()
# #root.resizable(False,False)
# root.geometry("250x250")
# root.minsize(50,50)
# sc=Scrollbar(root)
# sc.pack(side=RIGHT,fill=Y)
# mylist=Listbox(root,yscrollcommand=sc.set)
# for i in d:
#     mylist.insert(END,i)
# mylist.pack(fill=BOTH)
# Scrollbar(mylist,orient="vertical")
# sc.config(command=mylist.yview)
# root.mainloop()