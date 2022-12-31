# def outer():
#     print('outer function started')
#     def inner():
#         print('inner function execution')
#     print('outer funcion returning inner function')
#     return inner 

# outer()
# f1 = outer()
# f1()
# f1()
# f1()




#  Function Decorators:
# ------------------------------

# def decor(func):
#     def inner(name):
#         if name == 'Sunny':
#             print('Hello Sunny Bad Morning')
#         else:
#             func(name)
#     return inner


# # @decor
# def wish(name):
#     print('Hello', name, 'Good Morning')

# # wish('Anurag')
# # wish('Shanu')
# # wish('Sunny')

# decorfunction = decor(wish)

# wish('anurag')
# decorfunction('anurag')

# wish('Sunny')
# decorfunction('Sunny')
# ------------------


# Example-->

def smartdivision(func):
    def inner(a, b):
        if b==0:
            print('Hello Stupid...How we can divide widh zero')
        else:
            return func(a, b)     
    return inner


@smartdivision
def division(a, b):
    return a/b


print(division(10,2))
print(division(10,4))
print(division(10,0))






