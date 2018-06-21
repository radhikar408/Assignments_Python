# Q.4- Create a class Shape.Initialize it with length and breadth Create the method Area. Create class rectangle and square which inherits shape and access the method Area.
class shape:
	def __init__(self,l,b):
		self.length=l
		self.breadth=b
	def area(self):
		self.area=self.length*self.breadth
		print(self.area)
class rectangle(shape):
	pass
class square(shape):
	pass
s=square(2,2)
r=rectangle(2,4)
s.area()
r.area()