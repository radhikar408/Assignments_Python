#Q.6- Create a user-defined exception AgeTooSmallError() that warns the user when they have entered age less than 18. The code must keep taking input till the user enters the appropriate age number(less than 18).
class ValueTooSmallError(Exception):
	pass
while True:
	try:
		age=int(input("enter your age : "))
		if age<18:
			raise ValueTooSmallError("Exception")
		else:
			print("elligible")
			break
	except ValueTooSmallError as e:
		print(".........this value is too small ........ try again!!!!!!  ")
		print(e)