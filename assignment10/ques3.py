# Q.3- Create a class Cop. Initialize its name, age , work experience and designation. Define methods to add, display and update the following details. Create another class Mission which extends the class Cop. Define method add_mission _details. Select an object of Cop and access methods of base class to get information for a particular cop and make it available for mission.
class cop:
	def add(self,name,age,work,desig):
		self.name=name
		self.age=age
		self.work_ex=work
		self.desig=desig

	def display(self):
		print("your name is  ",self.name)
		print("your name is ",self.age)
		print("your name is ",self.work_ex)
		print("your name is ",self.name)
	def update(self,name,age,work,desig):
		self.name=name
		self.age=age
		self.work_ex=work
		self.desig=desig
	
class mission(cop):
	def add_mission_detail(self,mission):
		self.mission=mission
		print(self.mission)
		
m1=mission()
m1.add_mission_detail("assigned to HCL")
m1.add("abcd",22,3,"gateman")
m1.display()
m1.update("xyz",23,5,"manager")
m1.display()		