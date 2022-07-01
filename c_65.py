# Local Variable:
# ----------------------

# class Test:
#     def m1():
#         i = 0
#         while i<10:
#             print('Hello')
#             i = i+1
# Test.m1()


# class Test:
#     def m1():
#         a=10
#         print(a)
#     def m2():
#         b=20
#         a=888
#         print(b)
#         print(a)

# Test.m1()
# Test.m2()

# -----------------------------------------------


# Type of Methods:
# --------------------

# 1. Instance Methods:
# ---------------------

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#     def display(self):
#         print('Hi', self.name)
#         print('Your marks are: ', self.marks)
#     def grade(self):
#         if self.marks>=60:
#             print('You got First Grad')
#         elif self.marks>=50:
#             print('You got Second Grad')  
#         elif self.marks>=35:
#             print('You got Third Grad')   
#         else:
#             print('You are Failed')      

# n = int(input('Enter Number of Student: '))
# for i in range(n):
#     name = input('Enter Student Name: ')
#     marks =int(input('Enter Student Marks: '))
#     s = Student(name, marks)
#     s.display()
#     s.grade()


# Getter and Setter Method:
# --------------------------

# class Student:
#     def setName(self, name):
#         # validation logic
#         self.name = name

#     def getName(self):
#         return self.name

#     def setMarks(self, marks):
#         self.marks = marks

#     def getMarks(self):
#         return self.marks    

# n = int(input('Enter Number of Student: '))
# for i in range(n):
#     s = Student()
#     name = input('Enter Student Name: ')
#     s.setName(name)
#     marks =int(input('Enter Student Marks: '))
#     s.setMarks(marks)

#     print('Hi', s.getName())
#     print('Your marks are: ', s.getMarks())
#     print()




# 2. Class Methods:
# ------------------

# class Animal:
#     legs = 4
#     @classmethod
#     def walk(cls, name):
#         print('{} walks with {} legs'.format(name, cls.legs))

# Animal.walk('Dog')
# Animal.walk('Cat')


## Program to track the number of objects created for a class???
# ---------------------------------------------------------------

# class Test:
#     count=0
#     def __init__(self):
#         Test.count += 1

#     @classmethod    
#     def noOfObjects(cls):
#         print('The number of objects created', cls.count)    

# t1=Test()
# t2=Test()
# Test.noOfObjects()
# t3=Test()
# t4=Test()
# t5=Test()
# t5.noOfObjects()
# ------------------------------------------------------------




# 2. static Methods:
# ---------------------

# class DurgaMath:
#     @staticmethod
#     def add(x, y):
#         print('The Sum: ', x+y)

#     @staticmethod    
#     def product(x, y):
#         print('The Product: ', x*y)

#     @staticmethod    
#     def avg(x, y):
#         print('The Average: ', (x+y)/2)


# DurgaMath.add(10,20)
# DurgaMath.product(10,20)
# DurgaMath.avg(10,20)



class Test:
    count=0
    def __init__(self):
        Test.count += 1
  
    def noOfObjects():
        print('The number of objects created', Test.count)    

t1=Test()
t2=Test()
t3=Test()
t4=Test()
t5=Test()
Test.noOfObjects()




