# try with multiple except blocks:
# ---------------------------------

#-->
# try:
#     x = int(input('Enter First number: '))
#     y = int(input('Enter Second number: '))
#     print(x/y)
# except ZeroDivisionError:
#     print("Con't divide with zero")
# except ValueError:
#     print('Please provide int value only')    



# Single except block that can handle multiple exceptions:
# --------------------------------------------------------

#-->
# try:
#     x = int(input('Enter First number: '))
#     y = int(input('Enter Second number: '))
#     print(x/y)
# except (ZeroDivisionError, ValueError) as msg:
#     print(msg)



# Default except block:
# ----------------------

#-->
# try:
#     x = int(input('Enter First number: '))
#     y = int(input('Enter Second number: '))
#     print(x/y)
# except ZeroDivisionError:
#     print('ZeroDivisionError: cannot divide with zero')
# except:
#     print('default Except: plz provied valid input')


# finally block:
# ----------------

# try:
#     risky code
# except:
#     Handling code
# finally:
#     cleanup code



# -->
# try:
#     print('try')
#     print(10/0)
# # except ZeroDivisionError:
# except ValueError:
#     print('except block')
# finally:
#     print('finally block')



# Control flow of try-except-finally block:
# -----------------------------------------

# try:
#     stmt-1
#     stmt-1
#     stmt-1
# except XYZ:
#     stmt-1
# finally:        
#     stmt-1
# stmt-1











