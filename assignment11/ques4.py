#Q4. Call factorial function using thread.
import time
import threading 
from threading import Thread
def factorial():
	n=int(input("enter number whose factorial u want : "))
	fact=1
	for i in range(1,n+1):
		fact=fact*i
	print(fact)	

t=Thread(target=factorial)
t.start()
