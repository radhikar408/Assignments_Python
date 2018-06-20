#Q.1- Create a circle class and initialize it with radius. Make two methods getArea and getCircumference inside this class.
class Circle:
	radius=4
	def getArea(self):
		area=3.14*self.radius*self.radius
		print(area)
	def getCircumference(self):
		area2=(2*3.14*self.radius)
		print(area2)
r1=Circle()
r1.getArea()
r1.getCircumference()
