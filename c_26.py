# isalnum(), isdigit(), islower(), isupper(), istitle(), isspace():----------->
# only alphanumeric characters a-z, A-Z, 0-9

# a = 'anurag3434'
# print(a.isalnum())

# s = input('Enter any character: ')
# if s.isalnum():
#     print('Alpha Numeric character')
#     if s.isalpha():
#         print('Alphabet character')
#         if s.islower():
#             print('Lower case alphabet character')
#         else:
#             print('Upper case alphabet character')   
#     else:
#         print('it is a digit')
# elif s.isspace():
#     print('it is a space character')
# else:
#     print('Non Space Special Character')    

# ---------------------------------------------------


# Formating strings:

# name = 'Anurag'
# age = 22
# salary = 10000

# print("{}'s Age is {} aand his salary is: {}".format(name, age, salary))
# #or
# print(f"{name}'s Age is {age} aand his salary is: {salary}")



# Q. WAP to reverse the given string:

# s= 'anurag'
# 1.
# print(s[::-1])

# 2.
# n = len(s)
# i=-1
# while i>= -n:
#     print(s[i], end='')
#     i-= 1

# or 

# i = len(s) -1
# output = ''
# while i>=0:
#     output=output+s[i]
#     i = i-1
# print(output)    

# 3.
# for x in reversed(s):
#     print(x, end='')

# 4.
# print(''.join(reversed(s)))

#----------------------------------------------
# Q.
# input: Durga Software Solution
# output: Solution Software Durga

# s = 'Durga Software Solution'
# s = s.split()

# print(s[::-1])
# for x in reversed(s):
#     print(x, end=' ')

# l1 = []
# i = len(s)-1
# while i >= 0:
#     l1.append(s[i])
#     i -= 1
# output = '  '.join(l1) 
# print(output)   

# -------------------------------------

# Q.
# input: Durga Software Solution
# output: agruD erawtfoS noituloS

# s = 'Durga Software Solution'
# l = s.split()
# l1 = []
# for x in l:
#     l1.append(x[::-1])

# output = ' '.join(l1)
# print(output)


# -------------------------------------

# Q.
# Somthig:
# even index
# odd index

# Q.
# s1 = 'RAVI'
# s2 = 'TEJA'
# output: RTAEVJIA

# Q.
# input:B4A1D3
# output: ABD, 134

# Q. 
# input:a4b3c2
# output:aaaabbbcc

# Q. 
# input:a4k3b2
# output:aeknbd




