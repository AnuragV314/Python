# f = open('abc.txt', 'w')
# f.write('Sunny\n')
# f.write('Sunny1\n')
# f.write('Sunny2\n')
# f.write('Sunny3\n')
# f.close()
#--------------------------------------------------



# reading character data from the file:----->read(),read(n),readline(),readlines()
# -------------------------------------

# f = open('abc.txt','r')
# data = f.read()
# # print(type(data))
# print(data)


# data = f.read(10)
# print(data)

# print(f.readline(), end='')
# print(f.readline(), end='')
# print(f.readline(), end='')
# print(f.readline(), end='')


# list = f.readlines()
# # print(list)
# for line in list:
#     print(line, end='')

# f.close()


# The with statement:
# --------------------

# with open('abc.txt', 'w') as f:
#     f.write('Anurag\n')
#     f.write('Veram\n')
#     f.write('Shanu\n')
#     print('is File Closed?',  f.closed)

# print('is File Closed?',  f.closed)



# tell() :
# ----------
# f = open('abc.txt', 'r')
# print(f.tell())
# print(f.read(4))
# print(f.tell())
# print(f.read(5))
# print(f.tell())


# seek() : 
# ----------

# data = 'All students are STUPIDS'

# f = open('abc.txt', 'w')
# f.write(data)

# with open('abc.txt', 'r+') as f:
#     text = f.read()
#     print(text)
#     print('The Current Cursor Position: ', f.tell())
#     f.seek(17)
#     print('The Current Cursor Position: ', f.tell())
#     f.write('GEMS!!!')
#     print('The Current Cursor Position: ', f.tell())
#     f.seek(0)
#     text = f.read()
#     print('Data After Modification: ')
#     print(text)
    




# existance of file :---> os.path.isfile()
# -------------------
# import sys
# import os


# fname = input('Enter file name: ')
# if os.path.isfile(fname):
#     print('File Exists: ', fname)
#     f = open(fname, 'r')
# else:
#     print('File Not Exists', fname)    
#     sys.exit(0)

# print('The content pf the file is: ')
# data = f.read()
# print(data)
