# Q.
# import os

# fname = input('Enter a file name: ')

# if os.path.isfile(fname):
#     f = open(fname, 'r')
#     list = f.readlines()
#     print(f'Number of lines in {fname}: ', len(list))
#     f.seek(0)
#     data = f.read()
#     print(f'Number of character in {fname}: ', f.tell())
#     f.seek(0)
#     words = data.split()
#     print(f'Number of words in {fname}: {len(words)}')
# else:
#     print(f'{fname} not exits')



# --->
# my ex for info---->some confusion
# s = 'anurag kumar verma'.split()

# print(len(s))
# print(type(s))
# print(s[1])

# for i in range(len(s)):
#     print(s[i])
# <-----
# Question Done hihihihih
# ---------------------------------------------------



#       Handling binary data:
# --------------------------------

# read images --->
# f1 = open('Guido.jpg', 'rb')
# f2 = open('pic.jpg', 'wb')

# bytes = f1.read()
# f2.write(bytes)
# print('New Images is available with the name: pic.jpg')

# video files---->
# f1 = open('video.mp4', 'rb')
# f2 = open('cmatrix.mp4', 'wb')

# bytes = f1.read()
# f2.write(bytes)
# print('New Video is available with the name: cmatrix.mp4')




#       Handling CSV files: (csv--> )
# ------------------------------------

# write-->
# import csv

# with open('emp.csv', 'w', newline='') as f:
#     w = csv.writer(f) # returns csv writer objeect pointing to f
#     w.writerow(['ENO', 'ENAME', 'ESAL', 'EADD'])
#     n = int(input('Enter Number of Employees: '))
#     for i in range(n):
#         eno = int(input('Enter Enployee Number: '))
#         ename = input('Enter Employee Name: ')
#         esal = float(input('Enter Employee Salary: '))
#         eadd = input('Enter Employee Address: ')
#         w.writerow([eno, ename, esal, eadd])
# print('Total Employees data written to csv file successfully')


# read--->
# import csv

# f = open('emp.csv', 'r')
# r = csv.reader(f) # returns reader object

# data = list(r)
# print(type(data))
# print(data)

# for line in data:
#     for words in line:
#         print(words, "\t" , end='')
#     print()



# ---->
# csv to json
# -----------
# import pandas as pd
# df = pd.read_csv('emp.csv')
# df.to_json('emp1.json')
# <----



# Zipping and Unzipping files:
# ----------------------------











