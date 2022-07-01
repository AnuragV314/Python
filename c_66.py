# Passing members of one class to another class: 
# ----------------------------------------------

# class Employee:
#     def __init__(self, eno, ename, esal):
#         self.eno = eno
#         self.ename = ename
#         self.esal = esal
#     def display(self):
#         print('Employee Number: ', self.eno)
#         print('Employee Name: ', self.ename)
#         print('Employee Salary: ', self.esal)


# class Test:
#     def modify(emp):
#         emp.esal = emp.esal+1000
#         emp.display()


# e = Employee(100, 'anurag',10000)
# Test.modify(e)



# Inner classes/ Nested classes:
# ------------------------------

#
# class Outer:
#     def m1(self):
#         print('Outer class method')
#     class Inner:
#         def m2(self):
#             print('Inner class method')

# o = Outer()
# o.m1()

# i = o.Inner()
# i.m2()

# # i = Outer().Inner()
# # i.m2()

# # Outer().Inner().m2()



#
# class Person:
#     def __init__(self):
#         print('Person class constructor')
#         self.name = 'Anurag'
#         self.db = self.Dob()
#     def display(self):  
#         print('Name: ', self.name) 
#     class Dob:
#         def __init__(self):
#             print('Dob class constructor')
#             self.dd = 28 
#             self.mm = 12
#             self.yy = 1947
#         def display(self):
#             print('Dob={}/{}/{}'.format(self.dd, self.mm, self.yy))

# p = Person()
# p.display()

# p.db.display()


#
# class Human:
#     def __init__(self):
#         self.name = 'Sunny'
#         self.head = self.Head()
#         self.brain = self.Brain()
#     def display(self):
#         print('Hello ', self.name)    

#     class Head:
#         def talk(self):
#             print('Talking..........')

#     class Brain:
#         def think(self):
#             print('Thinking.........')


# h = Human()
# h.display()
# h.head.talk()
# h.brain.think()



# Garbage Collection:
# -------------------

# import gc

# print(gc.isenabled())

# gc.disable()

# print(gc.isenabled())

# gc.enable()

# print(gc.isenabled())








