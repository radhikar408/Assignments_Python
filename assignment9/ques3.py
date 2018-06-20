# Q.3- Create a Temprature class. Make two methods :
# 1. convertFahrenheit - It will take celsius and will print it into Fahrenheit.
# 2. convertCelsius - It will take Fahrenheit and will convert it into Celsius.

class temperature:
	def convertfahrenheit(self,c):
		print(((c*1.8)+32))
		
	def convertcelcius(self,f):
		print((f-32)*(0.5556))
c=int(input("enter value in celcius : "))
f=int(input("enter value in fahrenheit : "))
t1=temperature()
t1.convertfahrenheit(c)
t1.convertcelcius(f)
