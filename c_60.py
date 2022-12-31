#---------------------------------------------------
#                    OOP
#---------------------------------------------------


# class Student():
#     def read(self):
#         print('Reading Python....')

# s = Student()
# s.read()



# class Student():
#     def __init__(self, name, rollno, marks):
#         self.name = name
#         self.rollno = rollno
#         self.marks = marks

# s1 = Student('Anurag', 101, 40)
# print(s1.name, s1.rollno, s1.marks)

# s1 = Student('shanu', 101, 50)
# print(s1.name, s1.rollno, s1.marks)



# class Student():
#     def __init__(self, x, y, z):
#         self.name = x
#         self.rollno = y
#         self.marks = z

# s1 = Student('Anurag', 101, 40)
# print(s1.name, s1.rollno, s1.marks)

# s2 = Student('shanu', 101, 50)
# print(s2.name, s2.rollno, s2.marks)



# class Student():

#     '''This is Student class with required data'''
#     def __init__(self, x, y, z):
#         self.name = x
#         self.rollno = y
#         self.marks = z
#     def display(self):
#         print('student name: {}, rollno: {}, marks: {}'.format(self.name, self.rollno, self.marks))

# s1 = Student('Anurag', 101, 40)
# s1.display()

# s2 = Student('shanu', 101, 50)
# s2.display()
 
# print(s1.__doc__) 
# help(Student)

# print(s1.__dict__)
# print(s2.__dict__)




## Static Variable:
# -------------------

# class Student():
#     cname = 'DURGASOFT'
 
# s = Student()
# print(s.cname)
# print(Student.cname)


# class Student():
#     cname = 'DURGASOFT'
#     def m1(self):
#         self.cname = 'DURGASOFTWARE'
 
# # s1 = Student()
# # s1.cname = 'DURGASOFTWARE'

# # s2=Student()
# # print(s2.cname)

# # print(s1.cname)

# s1 = Student()
# s2 = Student()

# print(s1.cname)
# print(s2.cname)

# s1.m1()
# print(s1.cname)

