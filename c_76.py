# -----------------------
#  Polymorphism
# -----------------------

# Poly ---> Many 
# Morohs ---> Forms
#   One Name but Multiple Forms


# + operator 
# 10 + 20 = 30
# 'anu' + 'rag' ==> anurag
# (operator overloading)



# class P:
#     def marry(self):
#         print('Subba Luxmi')

# class C(P):
#     def marry(self):
#         print('Sunny')
# (method overloading)




# 1. Duck type Philosophy of python:
# ---------------------------------
"""
"if it walks like a duck and talk like a duck 
    then it is duck"
"""

# class Duck:
#     def talk(self):
#         print('Quack Quack Quack...')

# class Dog:
#     def talk(self):
#         print('Bow Bow Bow...')

# class Cat:
#     def talk(self):
#         print('Moew Moew Moew...')

# class Goat:
#     def talk(self):
#         print('Myaah Myaah Myaah...')


# l = [Duck(), Dog(), Cat(), Goat()]
# for obj in l:
#     obj.talk()




# hasattr(obj, 'attributename')
# -------------------------------

# class Duck:
#     def talk(self):
#         print('Quack Quack Quack...')

# class Dog:
#     def bark(self): # bark
#         print('Bow Bow Bow...')

# class Cat:
#     def talk(self):
#         print('Moew Moew Moew...')

# class Goat:
#     def talk(self):
#         print('Myaah Myaah Myaah...')


# l = [Duck(), Dog(), Cat(), Goat()]
# for obj in l:
#     if hasattr(obj , 'talk'):
#         obj.talk()
#     elif hasattr(obj, 'bark'):
#         obj.bark()



# 2. Overloading :
# ----------------
# a) operator Overlading :
# ----------------------- 

class Book:
    def __init__(self,pages):
        self.pages = pages

    def __add__(self, other):
        return self.pages + other.pages

    def __sub__(self, other):
        return self.pages - other.pages  

    def __gt__(self, other):
        return self.pages > other.pages  

    def __gt__(self, other):
        return self.pages < other.pages         

b1 = Book(100)
b2 = Book(300)
print('the total number of pages: ', b1+b2)
print('b1-b2: ', b1-b2)
print('b1>b2: ', b1>b2)
print('b1<b2: ', b1<b2)

