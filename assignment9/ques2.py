#Q.2- Create a Student class and initialize it with name and roll number. Make methods to :
#1. Display - It should display all informations of the student.
class student:
	def __init__(self):
		self.name="dua"
		self.roll=654
	def Display(self):
		print(self.name,self.roll)
#n=input("input name :")
#r=int(input("enter roll no : "))
s1=student()
s1.Display()