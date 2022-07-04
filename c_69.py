# class P:
#     a=8888
#     def m1(self):
#         self.a = 10


# class C(P):
#     def __init__(self):
#         super().m1()
#         print(super().a)   
#         print(self.a)
   
# c = C()


# 
# class P:
#     def __init__(self) -> None:
#         self.b=10
#     def m1(self):
#         self.b  = 7777

# class C(P):
#     def __init__(self):
#         self.b=20
#         print('Before: ', self.b)
#         super().__init__()
#         print('After: ', self.b)
#         super().m1()
#         print(self.b)
        
# c = C()


# Type of Inheritence:
# --------------------

# 1.Singel:
# ---------
# class P:
#     def m1(self):
#         print('Parent method..')

# class C(P):
#     def m2(self):
#         print('Child method..')

# c = C()
# c.m1()
# c.m2()


# 2. Multi level:
# ---------------

# class GF:
#     def m1(self):
#         print('Grand Father method..')

# class F(GF):
#     def m2(self):
#         print('Father method..')

# class C(F):
#     def m3(self):
#         print('Child method..')

# c = C()
# c.m1()
# c.m2()
# c.m3()


# 3. Hierarchical:
# ----------------
# class P:
#     def m1(self):
#         print('Parent method..')

# class C1(P):
#     def m2(self):
#         print('Child 1 method..')

# class C2(P):
#     def m3(self):
#         print('Child 2 method..')

# c1 = C1()
# c2 = C2()
# c1.m1()
# c1.m2()
# c2.m1()
# c2.m3()


# 4. Multiple:
# -------------

# 5. Hybrid:
# -------------