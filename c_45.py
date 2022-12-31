#1
# def countdown(num):
#     print('Start countdown')
#     while (num>0):
#         yield num
#         num = num -1


# values = countdown(10)
# for x in values:
#     print(x)


#2 To Generate First n numbera

# def firstn(num):
#     n = 1
#     while n<=num:
#         yield n 
#         n = n+1

# values = firstn(10)
# for x in values:
#     print(x)

#3 febonacci numbers
# 0,1,1,2,3,5,8,13,21........

# def fib():
#     a,b = 0, 1
#     while True:
#         yield a
#         a, b = b, a+b

# f = fib()
# for x in f:
#     if x >100:
#         break
#     print(x, end=',')


# n=10
# a, b = 0,1
# for i in range(n):
#     print(b)
#     a,b = b , a+b
# ---------------------------------------------------



# ------------------------------------------------------
#                            Module
# ------------------------------------------------------



x = 888
y = 999

def add(a,b):
    print('The Sum: ', a+b)

def product(a,b):
    print('The Product: ', a*b)

# def division(a,b):
#     print('The Sum: ', a+b)

# def substraction(a,b):
#     print('The Sum: ', a+b)




