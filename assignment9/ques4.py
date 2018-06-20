# **Q.4- Create a class MovieDetails and initialize it with Movie name, artistname,Year of release and ratings .
# Make methods to 
# 1. Display-Display the details.
# 2. Update- Update the movie details.
# Q.5- Create a class Expenditure and initialize it with expenditure,savings.Make the following methods. 
# 1. Display expenditure and savings 
# 2. Calculate total salary
# 3. Display salary
class moviedetails:
	def __init__(self):
		self.name="abcd"
		self.artistname="pqrs"
		self.year="2000"
		self.rating=4
	def display(self):
		print("movie name is %s"%(self.name))
		print("movie artist name is %s"%(self.artistname))
		print("movie name is %s"%(self.year))
		print("movie name is %s "%(self.rating))
		
	def update(self):
		self.name=input("enter new movie name " )
		self.artistname=input("enter new artist name ")
		self.year=input("enter new release year ")
		self.rating=input("enter rating ")
		
m1=moviedetails()
m1.display()
m1.update()
m1.display()
