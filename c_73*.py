# Method Resolution Order(MRO):
# -----------------------------

# C3 Algorithom:(NOTES)
# --------------

# class P1:pass
# class P2:pass
# class C(P1,P2):pass
# print(C.mro())




# class D: pass
# class E: pass
# class F: pass
# class B(D,E): pass
# class C(D,F): pass
# class A(B,C): pass

# print(D.mro())
# print(E.mro())
# print(F.mro())
# print(B.mro())
# print(C.mro())
# print(A.mro())



class A: pass
class B: pass
class C: pass
class X(A,B): pass
class Y(B,C): pass
class P(X,Y,C):pass
print(P.mro()) # PXAYBCO
 

