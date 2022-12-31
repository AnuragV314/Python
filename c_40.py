# Recursive Function
# ---------------------------
# ---> A function that call itself


# def factorial(n):
#     if n==0:
#         result=1
#     else:
#         result = n*factorial(n-1)    
#     return result
 
# print(factorial(0))
# print(factorial(5))




# Anonymous Functions:
# --------------------------
# without name 

# s = lambda n : n*n
# print(s(4))
# print(s(5))


# s = lambda a,b:a+b
# print('The sum of {} and {} is: {}'.format(2,3,s(2,3)))
# print('The sum of {} and {} is: {}'.format(4,5,s(4,5)))

# s = lambda a,b: a if a>b else b
# print('The biggest of {} and {} is: {}'.format(34,45,s(34,45)))

# print('The biggest of {} and {} is: {}'.format(34,45,s(34,45)))


# 1. filter()
# 2. map()
# 3. reduced()


# 1. filter()
# -------------------
# filter(function, sequence)

# def iseven(x):
#     if x%2==0:
#         return True
#     else:
#         False    

# l = [0,5,10,15,20]

# print(type(filter(iseven, l)))

# l1 = list(filter(iseven, l))
# print(l1)

# or 
# l = [0,5,10,15,20,25,30,35,40]
# l1 = list(filter(lambda x:x%2==0, l))
# print(l1)



# 2. map()
# -----------------------
# map(function, sequence)

# def double(x):
#     return x*2

# l = [1,2,3,4,5]  
# l1 = list(map(double, l))
# print(l1)

# or
# l = [1,2,3,4,5,6,7,8]  
# l1 = list(map(lambda x:x*2, l))
# print(l1)

# l1 = [1,2,3,4]  
# l2 = [10,20,30,40]
# l3 = list(map(lambda x,y:x*y, l1,l2))
# print(l3)



### l = [0,5,10,15,20,25,30,35,40]
### l1 = list(map(lambda x:x%2==0, l))
### print(l1)

