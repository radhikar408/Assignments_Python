def table(n,i):
	if(i>10):
		return(0)
	else:
		print("%d * %d=%d"%(n,i,n*i))
		table(i,i+1)
table(12,1)
