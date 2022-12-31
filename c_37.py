# ----------------------------------------------
#                 Functions
# ----------------------------------------------

# def wish(name):
#     print('Hello', name , 'Good Evening')

# wish('Anurag')


# def square(x):
#     print(f'Square of {x} is:', x**2)
# square(4)
# square(5)



# def add(a, b):
#     return a+b

# result = add(4, 5)
# print(result)

# print(add(5,6))


# def f1():
#     print('Hello')
# print(f1())



# Weather the given number is even or odd?

# def evenodd(n):
#     if n%2==0:
#         print(f'{n} Number is even')
#     else:
#         print(f'{n} Number is odd')    

# evenodd(45)
# evenodd(12)


# to find factorial of given number?

# import math
# print(math.factorial(5))

# def fact(n):
#     result = 1
#     while n>=1:
#         result = result*n
#         n = n - 1
#     return result    

# print(fact(5))

# for i in range(1,6):
#     print(f'The factorial of {i} is: {fact(i)}')




# def sum_sub(a, b):
#     sum = a+b
#     sub = a-b
#     return sum, sub

# x, y = sum_sub(100, 50)
# print('The Sum: ', x) 
# print('The Sub: ', y)    




# Type of arguments: 

# 1. Positional arguments
# 2. Keyword arguments
# 3. Default arguments
# 4. Variable length arguments

# 1.
# def sub(a,b):
#     print(a-b)
# sub(100, 10)

# 2. 
# def wish(name, msg):
#     print('hello', name, msg)

# wish(name='Anurag', msg='Good Morning')
# wish(msg='Good Morning', name='Anurag')
# wish('Anurag', msg='Good Morning')
# wish(msg='Good Morning', 'Anurag') #error

# 3.
# def wish(name='guest'):
#     print('Hello', name, 'Good Evening')

# wish('Anurag')
# wish()


def wish(marks, age, name='guest', msg='Good Morning'):
    print('{} {} {} {}'.format(name, age, marks, msg))

wish(50, 22)
wish(50, 22, 'Anurag', ' Tu kya kr rha hai yarr')


