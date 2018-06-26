# Q.2- Name and handle the exception occurred in the following program: 
# l=[1,2,3]
# print(l[3])


#name of the error--list index out of range	
#handling the error
try:
	li=[1,2,3]
	print(li[3])
except Exception as e:
	print(e)


