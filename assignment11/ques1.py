#Q1. Create a threading process such that it sleeps for 5 seconds and then prints out a message. Q2. Make a thread that prints numbers from 1-10, waits for 1 sec between Q3. Make a list that has 5 elements.Create a threading process that prints the 5 elements of the list with a delay of multiple of 2 sec between each display.
#Delay goes like 2sec-4sec-6sec-8sec-10sec
import time
import threading
from threading import Thread
def display():
	time.sleep(5)
	print("Hello world")
t=Thread(target=display)
t.start()
