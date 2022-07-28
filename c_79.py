from abc import *

# class DBInterface(ABC):
#     @abstractmethod
#     def connect(self):
#         pass

#     @abstractmethod
#     def disconnect(self):
#         pass
    


# class Oracle(DBInterface):
#     def connect(self):
#         print('Connecting the Oracle database....')

#     def disconnect(self):
#         print('Disconnecting to Oracle database....')    


# class MySql(DBInterface):
#     def connect(self):
#         print('Connecting the MySql database....')

#     def disconnect(self):
#         print('Disconnecting to MySql database....')    

# class Sybase(DBInterface):
#     def connect(self):
#         print('Connecting the Sybase database....')

#     def disconnect(self):
#         print('Disconnecting to Sybase database....')    


# dbname = input('Enter database name: ')
# classname = globals()[dbname]
# x=classname()
# x.connect()
# x.disconnect()





# class Printer(ABC):
#     @abstractmethod
#     def printit(self, text):
#         pass

#     @abstractmethod
#     def disconnect(self):
#         pass
    
# class EPSON(Printer):
#     def printit(self, text):
#         print('Printing from EPSON Printer....')
#         print(text)

#     def disconnect(self):
#         print('Disconnecting to EPSON Printer....')    


# class HP(Printer):
#     def printit(self, text):
#         print('Printing from HP Printer....')
#         print(text)

#     def disconnect(self):
#         print('Disconnecting to HP Printer....')    
   

# with open('config.txt', 'r') as f:
#     pname = f.readline()
# # print(globals())
# # print(globals()[pname])
# classname = globals()[pname]
# # print(classname)
# x = classname()
# x.printit('**********This is the data to print**************')
# x.disconnect()

# -----------------


# public, privete, protected variables:
# ---------------------------------------

# class Test:
#     def __init__(self):
#         self.__x = 10

#     def m2(self):
#         print(self.__x)   

# t=Test()
# # print(t.__x)  # Error 
# t.m2()



# class Test:
#     def __init__(self):
#         self.__x = 10
# t=Test()
# print(t._Test__x)  # access private variable




# return and save object (tostring):

# class Student:
#     def __init__(self, name, rollno):
#         self.name = name
#         self.rollno = rollno

#     def __str__(self):
#         return  f'Name: {self.name}, Rollno: {self.rollno}'

# s1 = Student('Ram', 101)
# s2 = Student('Shyam', 102)
# print(s1)
# print(s2)





# def f1():
#     print('module-1 function')

# if __name__ == '__main__':
#     f1()