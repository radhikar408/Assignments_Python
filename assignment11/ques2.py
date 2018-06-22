import threading
from threading import Thread
import time
def number():
	for i in range(1,11):
		print(i)
		time.sleep(1)
t=Thread(target=number)
t.start()