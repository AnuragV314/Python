# class Enployee:
#     def __init__(self, eno , ename):
#         self.eno = eno
#         self.ename = ename
#         print('Constructor execution....')
#     def display(self):
#         print('Employee No: ', self.eno)
#         print('Employee Name: ', self.ename)

# e1 = Enployee(100, 'shanu')
# e2 = Enployee(111, 'anurag')
# e1.display()
# e2.display()



# 1. Instance Variables:
# ----------------------

# class Student:
#     def __init__(self, n, rollno, marks):
#         self.name = n
#         self.rollno = rollno
#         self.marks = marks
#     def display(self):
#         print('Student Name: ', self.name)    
#         print('Student Rollno: ', self.rollno)
#         print('Student Marks: ', self.marks)
#         print()


# s1 = Student('anurag', 101, 50)
# s2 = Student('shanu', 102, 51)
# s3 = Student('anu', 103, 90)
# s1.display()
# s2.display()
# s3.display()
# print(s1.name, s1.rollno, s1.marks)

# print(s1.__dict__)



# class Test:
#     def __init__(self):
#         self.x=10
    
# t1 = Test()
# t2 = Test()
# print(t1.x, t2.x)

# t1.x=888
# print(t1.x, t2.x)



# class Test:
#     def __init__(self):
#         self.a=1000
#         self.b=2000
#     def m1(self):
#         self.c=3000
#         self.d=4000    

# t1 = Test()
# t1.m1()
# # print(t1.__dict__)
# print(t1.a, t1.b, t1.c, t1.d)
# t2 = Test()
# t2.a=8888
# t2.b=9999
# t2.c=7777
# print(t2.__dict__)



class SE:
    def __init__(self, name , age, tech):
        self.name = name
        self.age = age
        self.tech = tech

s1 = SE('Anurag', 21, 'Pyrhon')
s2 = SE('Shanu', 22, 'C')
s1.gf='Sunny'
s1.gf2='Mallika'
s2.brand='RC'
s2.brand2='KF'
print(s1.__dict__)
print(s2.__dict__)
