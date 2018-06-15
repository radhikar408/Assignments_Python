#create a dictionary
d={}
name=""
marks=""
for i in range(3):
	name=input("enter your name ")
	marks=(int(input("enter your marks ")))
	d[name]=marks
print("dictionary is ")
print(d)