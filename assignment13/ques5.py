#Q.5- Write a program to show and handle following exceptions: 
# 1. Import Error
# 2. Value Error
# 3. Index Error


#1--import error
try:
	import radhika
except Exception:
	print("caught an exception")

#2--Value error
# a=(input("enter any string"))
# print(int(a))
#solution:
try:
	a=(input("enter any string"))
	print(int(a))
except Exception:
	print("not possible")

#3--index error
try:
	li=[2,6,8,4,8]
	print(li[7])
except Exception as e:
	print(e)

