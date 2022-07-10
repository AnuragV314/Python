########################################
#          MULTI THREDING
########################################



# MainThread
# import threading
# print('current executing thread: ', threading.current_thread().getName())



# The ways of creating Thread in Pyhton
# --------------------------------------

# 1. Creating a Thread without using any class
# ---------------------------------------------
# from threading import *

# def display():
#     print('This code (display function) executing by Thread: ', current_thread().getName())

# t = Thread(target=display) # MainThread create child thread object
# t.start()  # MainThread starts child thread
# print('This code executing by Thread: ', current_thread().getName())



# from threading import *
# def display():
#     for i in range(10):
#         print('Child Thread')

# t = Thread(target=display)
# t.start()

# for i in range(10):
#     print('Main Thread')



# 2. Creating a Thread by etending Thread class
# ---------------------------------------------
# from threading import *

# class MyThread(Thread):
#     def run(self):
#         for i in range(10):
#             print('child thread-1')


# t = MyThread()
# t.start()

# for i in range(10):
#     print('main thread')




# 3. Creating a Thread without etending Thread class
# ---------------------------------------------

# from threading import *

# class Test:
#     def display(self):
#         for i in range(10):
#             print('child thread-1')

# obj=Test()
# t = Thread(target=obj.display)
# t.start()

# for i in range(10):
#     print('main thread')




# from threading import *
# class Test:
#     def display(self):
#         for i in range(10):
#             print('child thread executed by: ', current_thread().getName())

# obj=Test()
# t1 = Thread(target=obj.display)
# t2 = Thread(target=obj.display)
# t3 = Thread(target=obj.display)
# t4 = Thread(target=obj.display)
# t1.start()
# t2.start()
# t3.start()
# t4.start()





# import time
# from threading import *

# def doubles(numbers):
#     for n in numbers:
#         time.sleep(1)
#         print('double', 2*n)


# def squares(numbers):
#     for n in numbers:
#         time.sleep(1)
#         print('sqares: ', n*n)


# numbers = [1,2,3,4,5,6]
# begaintime = time.time()

# # doubles(numbers)
# t1 = Thread(target=doubles, args=(numbers,))
# # squares(numbers)
# t2 = Thread(target=squares, args=(numbers,))

# t1.start()
# t2.start()
# t1.join()
# t2.join()
# endtime = time.time()
# print('Total time taken: ', endtime-begaintime)




# get and set Thread Name:
from threading import *
print(current_thread().getName())
current_thread().setName('anurag')
print(current_thread().getName())










