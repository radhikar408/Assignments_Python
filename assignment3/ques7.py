#count the number of odd and even numbers
li=[1,2,3,4,5,6,7]
e=0
o=0
for i in range(0,9):
	if((li[i]%2)==0):
		e=e+1
	else:
		o=o+1
print(e)
print(o)