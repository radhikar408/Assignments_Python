#calculate the no of upper and lower case in a given string
s=input("enter an string  ")
c=0                                                #to count no of lower case letters
d=0												   #to count no of upper case letters
for i in s:
	if(i.islower()):
		c=c+1
	if(i.isupper()):
		d=d+1	
print(c)
print(d)

