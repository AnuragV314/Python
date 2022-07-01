# Nested try-except-finally:
# ----------------------------

#-->
# try:
#     print('outer try block')
#     try:
#         print('inner try block')
#         print(10/0)
#     except ZeroDivisionError:
#         print('inner except block')
#     finally:
#         print('inner finally block')           

# except:
#     print('outer except block')
# finally:
#     print('outer finnaly block')


# Control flow of Nested loop:
# ----------------------------------
# try:
#     stmt-1
#     stmt-2
#     stmt-3
#     try:
#         stmt-4
#         stmt-5
#         stmt-6
#     except XXXX:
#         stmt-7
#     finally:
#         stmt-8
#     stmt-9
# except YYYYY:
#     stmt-10                
# finally:
#     stmt-11
# stmt-12




# else block :
# -------------

# try:
#     pass
# except:
#     pass
# else:
#     pass
# finally:
#     pass


# --->
try:
    print('try')
    print(10/0) #<---
except:
    print('except')    
else:
    print('else')
finally:
    print('finally')












