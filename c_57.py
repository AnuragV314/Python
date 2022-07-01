# Zipping and Unzipping files:
# ----------------------------

# To create a zip file:-->

# from zipfile import *

# f = ZipFile('files.zip', 'w', ZIP_DEFLATED)
# f.write('a.txt')
# f.write('b.txt')
# f.write('c.txt')
# f.close()

# print('files.zip file created successfully')


# To perform unzip file:
# ------------------------

# from zipfile import *

# f = ZipFile('files.zip', 'r', ZIP_STORED)
# names = f.namelist()

# for name in names:
#     print('File Name: ', name)
#     print('The contant of this file: ')
#     f1 = open(name, 'r')
#     print(f1.read())
#     print()




# Working with Directories:
# ---------------------------
# S1: To know current working dirctories.
# import os
# cwd = os.getcwd()
# print('Current Working directory is : ', cwd)


# S2: To Create dirctories.
# import os
# cwd = os.mkdir('anurag')
# print('my directery is created successfully')


# S3: inside anurag dir we create pythonvideo dir.
# import os
# cwd = os.mkdir('anurag/pythonvideo')
# print('my directery is created successfully')


# S4: To create multiple sub directory.
# import os
# cwd = os.makedirs('sub1/sub2/sub3/sub4')
# print('sub dir create')


# S5: To remove directory.
# import os
# os.rmdir('anurag/pythonvideo')
# print('task completed')


# S6: To remove all directory.
# import os
# os.removedirs('sub1/sub2/sub3/sub4')
# print('task completed')


# S7: rename dir.
# import os
# os.rename('anurag', 'shanu')
# print('Task completed')


# S8: To know contents of dir.
# import os
# print(os.listdir('com'))
# print('Task completed')

# print(os.listdir('.')) # . means current dir


# S9: To know contents of dir and sub dir also.
import os
for dirpath, dirnames, filenames in os.walk('.'):
    print('Current Working Directory Path: ', dirpath)
    print('Directories: ', dirnames)
    print('File names: ', dirnames)
    print()
