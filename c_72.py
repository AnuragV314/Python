# --------------------------------------------
# --------------------------------------------
# class 68
# super(): some importent info.
# ----------------------------

# class P:
#     a = 10
#     def __init__(self):
#         self.b = 40
#         print('constructor..')
#     def m1(self):
#         print('instance method')
#     @classmethod       
#     def m2(cls):
#         print('class method')
#     @staticmethod    
#     def m3():
#         print('static method')


#instance method
# class C(P):
#     def m1(self):
#         print(super().a)
#         # print(super().b)  # error
#         print(self.b)
#         super().__init__()
#         super().m1()
#         super().m2()
#         super().m3()
# c=C()
# c.m1()

#constructor
# class C(P):
#     def __init__(self):
#         print(super().a)
#         super().__init__()
#         super().m1()
#         super().m2()
#         super().m3()  
# c=C()
# c.m1()

#class method
# class C(P):
#     @classmethod
#     def m1(cls):
#         print(super().a) 
#         # super().__init__()  # error
#         # super().m1()   # error
#         super().m2()
#         super().m3()     
# c=C()
# c.m1()

#static method
# class C(P):
#     @staticmethod
#     def m1():
#         # print(super().a)  # error
#         # super().__init__()  # error
#         # super().m1()   # error
#         # super().m2()
#         #super().m3() 
#         pass

# c=C()
# c.m1()


# 4.Multiple Inheritance:
# -----------------------
# class Father:
#     def height(self):
#         print('Height is 6 feet')
# class Mother:
#     def color(self):
#         print('brown color')
# class Child(Father, Mother):
#     pass        

# c = Child()
# print('Child inherited properties from parents')
# c.height()
# c.color()


# 
# class P1:
#     def m1(self):
#         print('P1 method')
# class P2:
#     def m1(self):
#         print('P2 method')

# class C(P1, P2):
#     pass        

# c = C()
# c.m1()

# 5.cyclic Inheritance: --> Not Allowed
# -----------------------

# 6.Hybrid Inheritance: --> Single + multi lvl + Multiple + Hierarchical
# ---------------------



# --------------------------------------------------
# --------------------------------------------------

# Method Resolution Order(MRO):---->
##################################

class D: pass
class E: pass
class F: pass
class B(D,E): pass
class C(D,F): pass
class A(B,C): pass
# print(A.mro())
print(B.mro())

 