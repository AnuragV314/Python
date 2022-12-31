# 3. reduced()
# --------------------
# from functools import *

# l = [10,20,30,40,50]
# result = reduce(lambda x,y: x+y, l)
# print(result)



#  everything in python is an object (except keywords)

# def f1():
#     print('Hello')

# print(f1)
# print(id(f1))

# print(id(print()))



# Function Aliasing --->
# ---------------------------


# def wish(name):
#     print(f'Good Morning: {name}')

# greeting = wish
# greeting('Shanu')
# wish('Anurag')

# print(id(wish))
# print((id(greeting)))

# del wish
# greeting('Shanu')




# Nested Function  --->
# ---------------------------


# def outer():
#     print('outer function started')
#     def inner():
#         print('inner function execution')
#     inner()    

# outer()


# def f1():
#     def inner(a,b):
#         print('The sum: ', a+b)
#         print('The Average: ', (a+b)/2)

#     inner(10,20)
#     inner(20,30)
#     inner(30,40)

# f1() 
# inner(10,20) # error











