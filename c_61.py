# class Student:
#     '''This is Student properties and actions'''
#     pass

# print(Student.__doc__) 
# # help(Student)


# class Student:
#     def __init__(self):
#         self.name = 'shanu'
#         self.rollno = 101
#         self.marks = 50
#     def talk(self):
#         print('hello My name is :', self.name)   
#         print('My rollno is :', self.rollno) 
#         print('My marks are :', self.marks) 


# s = Student()
# s.talk()




# class Test:
#     def __init__(self,):
#         print('constructor execution...')
#     def m1(self):
#         print('method execution...')    

# t1 = Test()
# t2 = Test()
# t3 = Test()
# t4 = Test()

# t1.m1()



# Constructor with multiple optional arguments:

# class Student:
#     def __init__(self, n='', m=0):
#         self.name=n
#         self.marks=m
#     def display(self):
#         print('Hi', self.name,)    
#         print('Marks: ', self.marks)


# s1 = Student()
# s1.display()

# s2 = Student('shanu', 50)
# s2.display()

# Constructor with mendatory arguments:

class Employee:
    def __init__(self, eno, ename, esal, eaddr):
        self.eno = eno
        self.ename = ename
        self.esal = esal
        self.eaddr = eaddr
    def display(self):
        print('Employee Number: ', self.eno)  
        print('Employee Name: ', self.ename)
        print('Employee Salary: ', self.esal)
        print('Employee Address: ', self.eaddr)  


e1 = Employee(101,'shanu', 1000, 'noida')
e1.display()




