p=[]
def perfect():
	for x in range(1,1000):
		li=[]
		sum=0
		for y in range(1,x):
			if(x%y==0):
				li.append(y)
		for a in li:
			sum=sum+a
		if(sum==x):
			p.append(x)
perfect()
print(p)
