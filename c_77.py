# overload > and <= operators for Student objects:===>

# class Student:
#     def __init__(self, name, marks):
#         self.name=name
#         self.marks = marks

#     def __gt__(self, other):
#         return self.marks > other.marks

#     def __le__(self, other):
#         return self.marks <= other.marks        


# s1= Student('Durga', 100)
# s2= Student('Ravi', 200)

# print('s1>s2: ', s1>s2)
# print('s1<=s2: ', s1<=s2)



#  overload * operators for Employee objects:===>

# class Employee:
#     def __init__(self, name , salary):
#         self.name = name
#         self.salary = salary 

#     def __mul__(self, other):
#         return self.salary * other.days  

# class TimeSheet:
#     def __init__(self, name, days):
#         self.name = name
#         self.days = days

# e = Employee('anurag', 100)
# t = TimeSheet('anurag', 25)        
# print('This month salary: ', e*t)


# oeder is imp.
# class Employee:
#     def __init__(self, name , salary):
#         self.name = name
#         self.salary = salary 

#     def __mul__(self, other):
#         return self.salary * other.days  

# class TimeSheet:
#     def __init__(self, name, days):
#         self.name = name
#         self.days = days

#     def __mul__(self, other):
#         return self.days * other.salary    

# e = Employee('anurag', 100)
# t = TimeSheet('anurag', 25)        
# print('This month salary: ', e*t) # oeder is imp.
# print('This month salary: ', t*e)




# b) Method Overlading :(Not available)
# ---------------------
# but indirectly achiive overloading

# class Test:
#     def m1(self):
#         print('No-arg method')

#     def m1(self, a):
#         print('One-arg method')

#     def m1(self,a, b):
#         print('Two-arg method')   

# t = Test()     
# # t.m1() # error
# # t.m1(2) # error       
# t.m1(2, 5)



# with Default arguments :

# class Test:
#     def sum(self, a=None, b= None, c= None):
#         if a!=None and b!=None and c!=None:
#             print('The Sum: ', a+b+c)
#         elif a!=None and b!=None:
#             print('The Sum: ', a+b)    
#         else:
#             print('Please provide 2 or 3 values only')    

# t = Test()
# t.sum(10,20)
# t.sum(10,20,30)
# t.sum()
# # t.sum(10,20,30,50) # error


# variable number of argument:

# class Test:
#     def sum(self, *n):
#         total = 0
#         for n1 in n:
#             total = total + n1
#         print('The Sum: ', total)    

# t = Test()
# t.sum()
# t.sum(10)
# t.sum(10,20)
# t.sum(10,20,30)





# c) Constructor Overlading :(Not available)
# ---------------------
# (same as method overloading)

# class Test:
#     def __init__(self):
#         print('No-arg constructor')

#     def __init__(self, a):
#         print('One-arg constructor')

#     def __init__(self, a, b):
#         print('Two-arg constructor')        

# # t = Test() #error
# # t = Test(1) #error
# t = Test(1, 2)

# ----------------------------------




# 3. Overriding:
# ------------------------
# a) Method Overriding:
# ---------------------

# class P:
#     def property(self):
#         print('Cash+Land+Gold+Power')

#     def marry(self):
#         print('Appalamma')

# class C(P):
#     def marry(self):
#         # super().marry()
#         print('Sunny')  


# c = C()
# c.property()
# c.marry()



# class Loan:
#     def interestrate(self):
#         return 10.5


# class Glone(Loan):
#     def interestrate(self):
#         return 14.5

# class Vlone(Loan):
#     def interestrate(self):
#         return 8.5



# b) Constructor Overriding:
# --------------------------

# class P:
#     def __init__(self):
#         print('Parent Constructor')

# # # class C(P):pass

# class C(P):
#     def __init__(self):
#         # super().__init__()
#         print('Child Constructor')
# c = C()




class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self, name, age, eno, esal):
        super().__init__(name, age)
        self.eno = eno
        self.esal = esal

    def display(self):
        print(f'Employee Name: {self.name}, Age: {self.age}, Eno: {self.eno}, Salary: {self.esal}')    



e = Employee('Anurag', 21, 234, 35000)
e.display()

e = Employee('Sunny', 22, 2344, 350000)
e.display()