from concurrent.futures import thread
from threading import*
import time
def f1():
    for x in range(5):
        print(current_thread().name,x)
t1=Thread(target=f1,name='tread1' )

def f2():
    for x in range(6,11):
        print(current_thread().name,x)
t2=Thread(target=f2,name="thread2")

t1.start()
t2.start()
print(current_thread().name)

