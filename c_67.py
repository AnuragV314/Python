# DC
# -----
#
# import time
# class Test:
#     def __init__(self):
#         print('Object Initialization...')

#     def __del__(self):
#         print('Fulfilling last wish and performing clean up activities...')   

# t1 = Test()
# t1 = None
# time.sleep(5)
# print('End of Application')


# 
# import time
# class Test:
#     def __init__(self):
#         print('Constructor Execution...')

#     def __del__(self):
#         print('Destructor Execution...')   

# t1 = Test()
# del t1
# time.sleep(5)
# print('End of Application')



# How to find numbers of references of an objects?:
# ----------------------------------------------
import sys
class Test:
    pass

t1 = Test()
t2 = t1
t3 = t1
t4 = t1
print(sys.getrefcount(t1)) # 5 (4 and self == 5)








