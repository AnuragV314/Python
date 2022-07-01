# The precess of identifying and fixing the bug ----> Debugging

# use print() statements  ----> after use delete



# assert statement:
# -----------------
#       1. simple version ---> assert conditional_expression
#       2. very simple version(augument version) ---> assert conditional_expression, massage
 

# assert ===> debugging


# ---->

# x = 10




# assert x == 10, 'here x value should be 10 but not'



# assert x > 10, 'here x value should be >10 but not'


# print(x)



# ---->
 
# def squareIt(x):
#     return x*x

# assert squareIt(2)==4, 'The square of 2 should be 4'
# assert squareIt(3)==9, 'The square of 2 should be 9'
# # assert squareIt(4)==16, 'The square of 2 should be 16'
# print(squareIt(2))
# print(squareIt(3))
# print(squareIt(4))



# Exception handling vs assertinons?
# ------------------------------------
# logging?
# ---------

# --------------------------------------------------------------



# ---------------------------------------------------
#                   File Hndling Concept
# ---------------------------------------------------

# open file --------->

# open(): --> # f = open(filename, mode)
# ---------

# f = open('abc.txt', 'r')

# print('File Name: ', f.name)
# print('File Mode: ', f.mode)
# print('File Readable?: ', f.readable())
# print('File writable?: ', f.writable())
# print('File Closed: ', f.closed)
# f.close()
# print('File Closed: ', f.closed)


# writing data to the text file:
# ------------------------------

# f = open('abcd.txt', 'a')
# f.write('Anurag\n')
# f.write('Veram\n')
# f.write('GG\n')
# print('Data write successfully to the file')



f = open('abcd.txt', 'w')
list = ['sunny\n', 'Bunny\n', 'chinny\n', 'vinny\n']
f.writelines(list)
print('Data write successfully to the file')




