#  ***** Inheritence and Polymorphism ***** :
# -----------------------------------------



# 1. Composition (Has-A Relationship) :
# -------------------------------------

#
# class Car:
#     def __init__(self, name, model, color):
#         self.name = name
#         self.model = model
#         self.color = color
#     def getinfo(self):
#         print(f'Car Name: {self.name}, Model: {self.model} and Color: {self.color}')


# class Employee:
#     def __init__(self, ename, eno, car):
#         self.ename = ename
#         self.eno = eno
#         self.car = car
#     def empinfo(self):
#         print('Employee Name: ', self.ename)
#         print('Employee Number: ', self.eno)
#         print('Employee Car Info: ')   
#         self.car.getinfo() 


# c = Car('BMW', 'M5', 'Red')
# e = Employee('Shanu', 101, c)
# e.empinfo()




# 2. Inheritence (Is-A Relationship) :
# -------------------------------------

#
# class X:
#     a = 10

# class Y(X):
#     pass

# y = Y()
# print(y.a)


#
# class X:
#     a = 10
#     def m1(self):
#         print('Parent class instance method')

# class Y(X):
#     pass
 
# y = Y()
# print(y.a)
# y.m1()


# 
# class X:
#     a = 10
#     def m1(self):
#         print('Parent class instance method')

#     @classmethod    
#     def m2(cls):
#         print('Parent class class method')

#     @staticmethod    
#     def m3():
#         print('Parent class static method')   

#     def __init__(self):
#         self.b=888
#         print('Parent Constructor.....')      

#     def __del__(self):
#         print('Parent Destructor.....')    

# class Y(X):
#     pass
 
# y = Y()
# print(y.a)
# y.m1()
# y.m2()
# y.m3()
# print(y.b)




# super() method:
# ---------------
#
# class X:
#     a = 10
#     def m1(self):
#         print('Parent class instance method')

#     @classmethod    
#     def m2(cls):
#         print('Parent class class method')

#     @staticmethod    
#     def m3():
#         print('Parent class static method')   

#     def __init__(self):
#         print('Parent Constructor.....')      


# class Y(X):
#     def __init__(self):
#         super().__init__()
#         print('child Constructor.....') 
#         super().m1() 
#         super().m2()
#         super().m3()
#         print(super().a)
# y = Y()



#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def eatndrink(self):
#         print('Biryani Eating and BEER Drinking') 

# class SE(Person):
#     def __init__(self, name, age, eno, esal):
#         super().__init__(name, age)
#         self.eno = eno
#         self.esal = esal
#     def work(self):
#         print('Python coding is somthing like chilled beer')


# s = SE('Anurag', 21, 100, 10000)
# print(s.name, s.age, s.eno, s.esal)
# s.eatndrink()
# s.work()



class A:
    x = 30
    def m1(self):
        self.x = 10
class B(A):
    def m1(self):
        super().m1()
        self.x = 20
    def dips(self):
        print(self.x)
        print(super().x)            
b = B()
b.m1()
b.dips()








