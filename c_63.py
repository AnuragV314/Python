# remove instance variable

# class Test:
#     def __init__(self):
#         self.a=10
#         self.b=20
#         self.c=30
#         self.d=40

# t1 = Test()
# t2 = Test()

# del t1.c
# del t2.d
# print('t1: ', t1.__dict__)
# print('t2: ', t2.__dict__)
# -------------------------------------


# 2. static variable:
# -------------------

# class Test:
#     a= 10
#     def __init__(self):
#         self.b = 20

# t = Test()
# print(t.a, t.b)
# print(Test.a, t.b)


# t1 = Test()
# t2 = Test()
# print('t1: ', t1.a, t1.b)
# print('t2: ', t2.a, t2.b)
# Test.a = 888
# t1.b = 999
# print('t1: ', t1.a, t1.b)
# print('t2: ', t2.a, t2.b)



#varias places to declare static variable?:

# class Test:
#     a=10
#     def __init__(self):
#         self.b = 20
#         Test.c = 30
#     def m1(self):
#         self.d = 40
#         Test.e = 50
#     @classmethod    
#     def m2(cls):
#         cls.f = 60    
#         Test.g = 70

#     @staticmethod
#     def m3():
#         Test.h = 80


# t = Test()
# t.m1() 
# Test.m2()
# Test.m3()
# Test.i = 90
# # print(Test.__dict__)
# print(t.a,t.c, t.e, t.f, t.g, t.h, t.i)
# print(Test.a, Test.c, Test.e, Test.f, Test.g, Test.h, Test.i)


# how to access static variable?:

# class Test:
#     a=10
#     def __init__(self):
#         print(self.a)
#         print(Test.a)
#     def m1(self):
#         print(self.a)
#         print(Test.a)
#     @classmethod    
#     def m2(cls):
#         print(cls.a)
#         print(Test.a)
#     @staticmethod
#     def m3():
#         print(Test.a)

# t = Test()
# t.m1() 
# Test.m2()
# Test.m3()
# print(t.a)
# print(Test.a)



# changing the value of static variable (places):
 
# class Test:
#     a = 10
#     def __init__(self):    
#         self.b = 20

# t1 = Test()
# t2 = Test()
# t1.a = 888 # it create a instance variable not assign on 'a'(=10 static variable)
# t1.b = 999
# print(t2.a, t2.b)
# print(t1.a, t1.b)

# print(t1.__dict__)
# print(t2.__dict__)


# t1 = Test()
# t2 = Test()
# Test.a = 888 # change a static variable
# t1.b = 999
# print(t2.a, t2.b)
# print(t1.a, t1.b)

# print(t1.__dict__)
# print(t2.__dict__)



