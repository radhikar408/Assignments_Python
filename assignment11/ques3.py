#Q3. Make a list that has 5 elements.Create a threading process that prints the 5 elements of the list with a delay of multiple of 2 sec between each display.
#Delay goes like 2sec-4sec-6sec-8sec-10sec
import time
from threading import Thread
import threading
def display(li):
	k=2
	for i in li:
		print(i)
		time.sleep(k)
		k=k+2
	





li=[1,2,3,4,5]
t=Thread(target=display,args=(li,))
t.start()