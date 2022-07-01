# Exceptions: ---->
# --------------
'''Exceptions are raised when the program is 
syntactically correct, but the code resulted 
in an error. This error does not stop the execution 
of the program, however, it changes the normal 
flow of the program.'''


# Type of error are possible
# 1. Syntax Errors
# 2. Runtime Errors


# 1.

# x = 10
# if x==10
#     print('x value is 10')

# SyntaxError: expected ':'


# 2.
# print(10/'ten')

# ...
# ...
# ...
# ...
# ...



# Customise Exception Handling by using try-except:
# ------------------------------

# print('stmt-1')
# try:
#     print(10/0)
# except ZeroDivisionError:
#     print(10/2)
# print('stmt-3')    


# control flow in try-except block:
# -------------------------------------


# print('stmt-1')
# try:
#     print('stmt-2')
#     print('stmt-3')
# except BaseException:
#     print('stmt-4')

# print('stmt-5')



# How to print exception information:
# -------------------------------------
try:
    print(10/0)
except ZeroDivisionError as msg:
    print("Exception rise and it's discreption is: ", msg)


