#Q.2- Write a Python program to count the frequency of words in a file. Q.3- Write a Python program to copy the contents of a file to another file Q.4- Write a Python program to combine each line from first file with the corresponding line in second file.
f=open("file1.txt",'r')
d={}
for word in f.read().split():
	if word not in d:
		d[word]=1
	else:
		d[word]+=1
for i,j in d.items():
	print(i,j)