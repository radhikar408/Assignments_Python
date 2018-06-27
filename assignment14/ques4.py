#Q.4- Write a Python program to combine each line from first file with the corresponding line in second file.
with open('file1.txt','r')as f1:
	with open('file2.txt','r')as f2:
		with open('file3.txt','w')as f3:
			file_1=f1.readlines()
			file_2=f2.readlines()
			for x in range(len(file_2)):
				f3.write(file_1[x]+file_2[x])