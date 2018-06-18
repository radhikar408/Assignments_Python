def power(b,p):
	s=1
	if p==1:
		return b
	else:
		s=b*power(b,p-1)
		return s
print(power(5,3))