# some revision
# -------------


#  <=== : Synchronization : ===>
# -------------------------------

# from threading import *
# import time

# def wish(name):
#     for i in range(10):
#         print('Good Evening: ', end='')
#         time.sleep(2)
#         print(name)

# t1 = Thread(target = wish, args=('Dhoni',))
# t2 = Thread(target = wish, args=('Kohli',))
# t1.start()
# t2.start()




# 1. Lock
# 2. RLock
# 3. Semaphore

# 1. Synchronization By using Lock concept:
# -----------------------------------------

# from threading import *
# import time

# l = Lock()

# def wish(name):
#     l.acquire()

#     for i in range(10):
#         print('Good Evening: ', end='')
#         time.sleep(2)
#         print(name)

#     l.release()    

# t1 = Thread(target = wish, args=('Dhoni',))
# t2 = Thread(target = wish, args=('Kohli',))
# t1.start()
# t2.start()

 

# from threading import *
# l = Lock()

# # print('main threading acquiring the lock...')
# # l.acquire()
# print('main threading releasing the lock...')
# l.release()





# 2. Synchronization By using RLock concept:
# ------------------------------------------
# from  threading import *

# l = Lock()

# print('Main thread trying to acquire lock ...')
# l.acquire()
# print('Main thread trying to acquire lock again...')
# l.acquire()
# print('Main thread acquire same lock again...')



# from  threading import *

# l = RLock()

# print('Main thread trying to acquire lock ...')
# l.acquire()
# print('Main thread trying to acquire lock again...')
# l.acquire()
# print('Main thread acquire same lock again...')



from threading import *

l = RLock()
def factorial(n):
    l.acquire()

    if n==0:
        result=1
    else:
        result=n*factorial(n-1)   

    l.release()    
    return result


def results(n):
    print('The factorial of n is', n,'is: ', factorial(n))

t1 = Thread(target=results, args=(5,))
t2 = Thread(target=results, args=(9,))
t1.start()
t2.start()

