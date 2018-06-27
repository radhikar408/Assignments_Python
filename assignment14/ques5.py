# Q.5- Write a Python program to write 10 random numbers into a file. Read the file and then sort the numbers and then store it to another file.
import random
import os
os.remove('sorted.txt')
li=[]
for i in range(100):
	li.append(i)
random.shuffle(li)
with open ('unsorted.txt','w')as f:
	for x in range(10):
		f.write(str(li[x])+'\n')
with open('unsorted.txt','r')as f1:
	with open('sorted.txt','w')as f2:
		content=f1.readlines()
	
		for i in range(len(content)):
			content[i]=int(content[i])
		content.sort()
		for i in range(len(content)):
			f2.write(str(content[i])+'\n')