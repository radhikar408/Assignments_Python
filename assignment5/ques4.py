n=int(input("enter an number between 1-200   "))
p1="no prize"
p2="Wooden Dog"
p3="Book"
p4="Chocolates"
if((n>1)and(n<50)):
	print("Congratulations!you have won %s"%(p1))
elif((n>51)and(n<150)):
		print("Congratulations!you have won  %s"%(p2))
elif((n>150)and(n<180)):
		print("Congratulations!you have won %s"%(p3))
elif((n>180)and(n<200)):
		print("Congratulations!you have won %s"%(n,p4))
elif(n>200):
	print("incorrect number")
else:
	print("Sorry! No prize this time.")

