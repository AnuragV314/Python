#1
# def decor(func):
#     def inner(name):
#         if name == 'Sunny':
#             print('Hello Sunny Bad Morning')
#         else:
#             func(name)    
#     return inner        


# @decor
# def wish(name):
#     print('Hello', name, 'Good Morning')

# wish('Anurag')
# wish('Shanu')
# wish('Sunny')




#2
# def decor1(func):
#     def inner(name):
#         print('Decorator_1 executing...')
#         func(name)
#     return inner    

# def decor2(func):
#     def inner(name):
#         print('Decorator_2 executing...')
#         func(name)
#     return inner

# @decor1
# @decor2
# def wish(name):
#     print('Hello', name, 'Good Morning')

# wish('Shanu')


#3
# def doubledecor(func):
#     def inner():
#         x = func()
#         return 2*x 
#     return inner    

# def squaredecor(func):
#     def inner():
#         x = func()
#         return x*x 
#     return inner 


# @squaredecor
# @doubledecor
# def num():
#     return 10

# print(num())
# -------------------------------------------------------------




# Generators:
# ----------------
# def mygen():
#     yield 'A'
#     yield 'B'
#     yield 'C'
#     yield 'D'

# g = mygen()
# print(type(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

# for x in g:
#     print(x)



def countdown(num):
    print('Start countdown')
    while (num>0):
        yield num
        num = num -1


values = countdown(10)
for x in values:
    print(x)
