# os module :
# -----------

#  system(): ---> os.system('command string')
# -----------------------------------------

# import os
# os.system('dir *.py')
# os.system('code')


# How to get information about a file:
# ------------------------------------
# import os 
# from datetime import *

# stats = os.stat('abc.txt')
# # print(stats)
# print('File size in bytes: ', stats.st_size)
# print('File Last accessed Time: ', datetime.fromtimestamp(stats.st_atime))
# print('File Last modified Time: ', datetime.fromtimestamp(stats.st_mtime))
# print('File Last Header modified Time: ', datetime.fromtimestamp(stats.st_ctime))





# ****   Pickling and unpickling of objects   ****:
# -------------------------------------------------

# pickle module:
# -------------

class Employee:
    def __init__(self, eno, ename, esal, eaddr):
        self.eno = eno
        self.ename = ename
        self.esal = esal
        self.eaddr = eaddr

e = Employee('100', 'Anurag', 5000, 'UP')
print(e.eno, e.ename, e.esal, e.eaddr)
