#  <==: Working with MySql Database :==>
# -----------------------------------------

# import pymysql

# try:
#     con = pymysql.connect(host='localhost', database='durgadb', user='root', password='password')
#     # print(con)
#     cursor = con.cursor()
#     # cursor.execute("create table employees1(eno int(5) primary key, ename varchar(10), esal double(10,2), eaddr varchar(10))")
#     # print('Table created...')

#     query = "insert into employees1(eno, ename, esal, eaddr) values(%s, %s, %s, %s)"


#     records = [(111, 'Katrina', 1111, 'Noida'),
#                 (222, 'Karina', 2222, 'Noida'),
#                 (333, 'Deepika', 3333, 'Noida'),
#                 (444, 'Priyanka', 4444, 'Noida'),
#     ]
#     cursor.executemany(query, records)
#     con.commit()
#     print('Records inserted into database')

#     cursor.execute('select * from employees1')
#     data = cursor.fetchall() 
#     for row in data:
#         print('Employee Number: ', row[0])
#         print('Employee Nmae: ', row[1])
#         print('Employee Salary: ', row[2])
#         print('Employee Address: ', row[3])
#         print()


# except pymysql.DatabaseError as e:
#     if con:
#         con.rollback()
#         print('There is problem: ', e)

# finally:
#     if cursor:
#         cursor.close()
#     if con:
#         con.close()    
 









# Connect MySql to Oracle : (readagain)
# -------------------------

# import pymysql
# import cx_Oracle

# try:
#     con = pymysql.connect(host='localhost', database='durgadb', user='root', password='password')

#     cursor = con.cursor()
#     cursor.execute('select * from employees')
#     data = cursor.fetchall() 
#     list = list(data)
#     print(list)

# except pymysql.DatabaseError as e:
#     if con:
#         con.rollback()
#         print('There is problem: ', e)

# finally:
#     if cursor:
#         cursor.close()
#     if con:
#         con.close()


# half code ......