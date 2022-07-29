# 3. Synchronization By using "Semaphore" concept:
# ------------------------------------------------

# from threading import *
# import time

# s = Semaphore(3)

# def wish(name):
#     s.acquire()
#     for i in range(10):
#         print('Good Evening: ', end='')
#         time.sleep(2)
#         print(name)
#     s.release()    

# t1= Thread(target=wish, args=('Dhoni',))
# t2= Thread(target=wish, args=('Kohli',))
# t3= Thread(target=wish, args=('Raina',))
# t4= Thread(target=wish, args=('Rohit',))

# t1.start()
# t2.start()
# t3.start()
# t4.start()



# from threading import *
# s = Semaphore(2)
# s.acquire()
# print('Main thread trying to acquire again...')
# s.acquire()
# print('Done1')
# # s.acquire() # error



# BoundedSemaphore:
# -----------------

# from threading import *
# s = Semaphore(2)
# s.acquire()
# s.acquire()
# s.release()
# s.release()
# s.release()
# s.release()
# s.release()
# s.release()

# but 

# from threading import *
# s = BoundedSemaphore(2)
# s.acquire()
# s.acquire()
# s.release()
# s.release()
# s.release()
# s.release()

# ---------


#    <=== Interthread Communication ====> :
# -----------------------------------------

# 1. Interthread Communication by using Event:
# --------------------------------------------


# from threading import *
# import time
# e = Event()
# def consumer():
#     print('Consumer Thread waiting for updation...') #Line-1
#     e.wait()
#     print('Consumer got notification and consuming items...')#Line-4

# def producer():
#     time.sleep(5)
#     print('Producer thread producing items..')#Line-2
#     print('Producer thread giving notification by setting event..')#Line-3
#     e.set()

# t1 = Thread(target=producer)
# t2 = Thread(target=consumer)
# t1.start()
# t2.start()





# from threading import *
# import time
# e = Event()

# def trafficpolice():
#     while True:
#         time.sleep(10)
#         print('Traffic police giving GREEN signal')
#         e.set()
#         time.sleep(20)
#         print('Traffic police giving RED signal')
#         e.clear()

# def driver():
#     num = 0
#     while True:
#         print('Drivers waiting for Green signal')
#         e.wait()
#         print('Traffic signal GREEN... Vehicles can move')
#         while e.isSet():
#             num=num+1
#             print('Vahicle Number: ', num, 'Crossing the signal')
#             time.sleep(2)
#         print('Traffic signal is RED....Drivers have to wait')    

# t1 = Thread(target=trafficpolice)
# t2 = Thread(target=driver)
# t1.start()
# t2.start()




# from threading import *
# import time
# def wish(name):
#     for i in range(10):
#         print('Good evening: ',flush=True ,end='')
#         time.sleep(2)
#         print(name)

# t1=Thread(target=wish, args=('Dhoni',))
# # t2=Thread(target=wish, args=('Anurag',))
# t1.start()
# -------------




# 2. Interthread Communication by using Condition object:
# -------------------------------------------------------

# from threading import *

# def consume(c):
#     c.acquire()
#     print('Consumer waiting for updation...')#Line-1
#     c.wait()
#     print('Consumer got notification & consuming the item...')#Line-4
#     c.release()

# def produce(c):
#     c.acquire()
#     print('Producer producing item...')#Line-2
#     print('Producing giving the notification')#Line-3
#     c.notify()
#     c.release()

# c = Condition()

# t1= Thread(target=consume, args=(c, ))
# t2= Thread(target=produce, args=(c, ))
# t1.start()
# t2.start()


 


from threading import *
import time
import random

items = []

def produce(c):
    while True:
        c.acquire()
        item = random.randint(1, 100)
        print('Producer producing the item: ', item)
        items.append(item)
        print('Producer giving notification')
        c.notify()
        c.release()
        time.sleep(5)

def consume(c):
    while True:
        c.acquire()
        print('Consumer waiting for updation...')
        c.wait()
        print('Consumer got notification & consuming the item...', items.pop())
        c.release()
        time.sleep(5)


c = Condition()

t1= Thread(target=consume, args=(c, ))
t2= Thread(target=produce, args=(c, ))
t1.start()
t2.start()

