d={}
name=""
marks=""
li=[]
for i in range(10):
	name=input("enter your name ")
	marks=(int(input("enter your marks ")))
	d[name]=marks
	li.append(marks)
	d[name]=marks
print("dictionary is ")
print(d)
print(li)
li.sort()
print(li)