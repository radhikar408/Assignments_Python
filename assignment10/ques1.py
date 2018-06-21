# Q.1- Create a class Animal as a base class and define method animal_attribute. Create another class Tiger which is inheriting Animal and access the base class method.
class animal:
	def animal_attribute(self):
		print("class animal")
		
class tiger(animal):
	def show(self):
		pass
d=tiger()
d.animal_attribute()