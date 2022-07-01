# 4. Variable length arguments ---> notes
# ------------------------------------------------
# variable length arguments:

# def f1(*args):
#     pass


# def sum(*n):
#     print(n)

# sum(23)
# sum(23,345)
# sum(23,345,45)
# sum(23,345,45,64,334)

# Keywards variable length arguments: 

# def f1(**kwargs):
#     pass


# def display(**kwargs):
#     print('Recard Information')
#     for k,v in kwargs.items():
#         print(k ,'.......', v)

# display(name='Anurag', marks=50, age=22, GF='Sunny')
# display(name='Shanu', wife1='abc', wife='xyz', wife3='klm')

# -------

# def f1(arg1,arg2,arg3=4,arg4=8):
#     print(arg1,arg2,arg3,arg4)


# f1(3,2)
# f1(10,20,30,40)
# f1(25,50,arg4=100)
# f1(arg4=2, arg1=3, arg2=4)
# f1() # error
# f1(arg3=10,arg4=40, 20, 12) # error
# f1(4,5,arg2=6) #error
# f1(4,5,arg3=5, arg5=5) # error


