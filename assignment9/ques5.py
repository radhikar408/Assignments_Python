# Q.5- Create a class Expenditure and initialize it with expenditure,savings.Make the following methods. 
# 1. Display expenditure and savings 
# 2. Calculate total salary
# 3. Display salary

class expenditure:
	def __init__(self):
		self.expen=1500
		self.saving=500
	def display(self):
		print("expenditure is %d and savings are %d"%(self.expen,self.saving))
	def calculate(self):
		self.sal=self.expen+self.saving
		print("salary is %d "%(self.sal))
e1=expenditure()
e1.display()
e1.calculate()
