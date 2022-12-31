# Decorator chaining:---> you can use many decoretor on one function
# --------------------------
#1
# def decor(func):
#     def inner(name):
#         print('First Decor (decor) Function Execution')
#         func(name)
#     return inner   


# def decor1(func):
#     def inner(name):
#         print('Second Decor (decor1) Function Execution')
#         func(name)
#     return inner


# @decor
# @decor1
# def wish(name):
#     print('Hello', name, 'Good Morning')

# wish('Anurag')



#2
# def decor1(func):
#     def inner():
#         x = func()
#         return x*x
#     return inner    

# def decor(func):
#     def inner():
#         x = func()
#         return 2*x
#     return inner   


# @decor
# @decor1
# def num():
#     return 10

# print(num())

# -----------------------------------------------------
# don't run

# l = [x*x for x in range(10000000000000000000000000)]
# print(l[0])
# print(l[1])
# print(l[2])


# l = [x*x for x in range(1000000000000000000)]
# print(next(l))
# print(next(l))
# print(next(l))
# print(next(l))
# ---------------------------------------------------



# l = [x*x for x in range(1000000000000000000)]
# l = (x*x for x in range(1000000000000000000))#====> Generators






















