# Thred Identification Number(ident):
# -----------------------------------

# from threading import *

# def display():
#     print('Child Thread')

# t = Thread(target=display)
# t.start()

# print('Main Thread Identification Number: ', current_thread().ident)
# print('Child Thread Identification Number: ', t.ident)



# active_count():
# ----------------
# from threading import *
# import time
# def display():
#     print(current_thread().name, 'started....')
#     time.sleep(3)
#     print(current_thread().name, 'ended...')

# print('the number of active threads: ', active_count())
# t1 = Thread(target=display, name='Child Thread 1')
# t2 = Thread(target=display, name='Child Thread 2')
# t3 = Thread(target=display, name='Child Thread 3')
# t1.start()
# t2.start()
# t3.start()
# print('the number of active threads: ', active_count())
# time.sleep(10)
# print('the number of active threads: ', active_count())



# list of all active thread objects:
# ----------------------------------
# enumerate():


# from threading import *
# import time
# def display():
#     print(current_thread().name, 'started....')
#     time.sleep(3)
#     print(current_thread().name, 'ended...')

# print('the number of active threads: ', active_count())
# t1 = Thread(target=display, name='Child Thread 1')
# t2 = Thread(target=display, name='Child Thread 2')
# t3 = Thread(target=display, name='Child Thread 3')
# t1.start()
# t2.start()
# t3.start()

# l = enumerate()
# for t in l:
#     print('Name: ', t.name)

# time.sleep(10)

# print('After 10 seconds sleeping...')
# l = enumerate()
# for t in l:
#     print('Name: ', t.name)



# is_alive()
# ----------

# from threading import *
# import time
# def display():
#     print(current_thread().name, 'started....')
#     time.sleep(3)
#     print(current_thread().name, 'ended...')

# print('the number of active threads: ', active_count())
# t1 = Thread(target=display, name='Child Thread 1')
# t2 = Thread(target=display, name='Child Thread 2')
# t3 = Thread(target=display, name='Child Thread 3')
# t1.start()
# t2.start()
# t3.start()

# print(t1.name, 'is Alive ', t1.is_alive() )
# print(t2.name, 'is Alive ', t2.is_alive() )
# print(t3.name, 'is Alive ', t3.is_alive() )

# time.sleep(10)

# print(t1.name, 'is Alive ', t1.is_alive() )
# print(t2.name, 'is Alive ', t2.is_alive() )
# print(t3.name, 'is Alive ', t3.is_alive() )



# join method:
# ------------

# from threading import *
# import time 

# def display():
#     for i in range(10):
#         print('Seetha Thread')
#         time.sleep(2)



# t = Thread(target=display)
# t.start()

# t.join(10)
# for i in range(10):
#         print('Rama Thread')





# Deamon Threads:
# ---------------

# from threading import *

# print(current_thread().isDaemon())

# def job():
#     print('Child Thread')


# t = Thread(target=job)
# print(t.isDaemon())
# t.setDaemon(True)
# t.start()
# print(t.isDaemon())



# from threading import *
# import time

# def job():
#     for i in range(10):
#         print('lazy Thread')
#         time.sleep(3)


# t = Thread(target=job)
# # t.setDaemon(True)
# t.start()
# time.sleep(5)
# print('End of Main Thread')



from threading import *
import time

def job1():
    print('job 1 execution....')
    print(current_thread().name, 'is deamon', current_thread().daemon)
    ct = Thread(target=job2, name='Child Thread 2')
    print('t is deamon: ', ct.daemon)

def job2():
    print('job 2 execution....')

t = Thread(target=job1, name='Child Thread')
t.setDaemon(True)
t.start()
time.sleep(10)
