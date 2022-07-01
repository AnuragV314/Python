
## 1. conditional statements ---> if, if-else, if-elif-else


## Program to find of biggest of given 3 numbers from the keyboard ???

# n1 = eval(input('Enter First Number: '))
# n2 = eval(input('Enter Second Number: '))
# n3 = eval(input('Enter Third Number: '))

# if n1>n2 and n1>n3:
#     print('Biggest number is: ', n1)
# elif n2>n3:
#         print('Biggest number is: ', n2)
# else:
#     print('Biggest number is: ', n3)



## Write a program to check weather the given number is in between 1 to 100 ???

# n = int(input('Enter a number: '))
# if n in range(1,100):
#     print('Number {} is in between 1 to 100'.format(n))
# else:
#     print('Number {} is not in between 1 to 100'.format(n))
   

# n = int(input('Enter a number: '))
# if n in range(1,100):
#     print(f'Number {n} is in between 1 to 100')
# else:
#     print(f'Number {n} is not in between 1 to 100')




## 2. Iterative statements --->(loop) for, while

# for loop ----->

# n='Anurag'
# count = 0
# for i in n:
#     count +=1
#     print(i)
# print('Number of character: ', count)


# s= input('Enter some string: ')
# i = 0
# for x in s:
#     if i!=0:
#         print('The character present at',i,'index is', x)
#     i += 1  

# for i in range(10):
#     print('Hello')


# for i in range(20):
#     if (i%2) != 0: 
#         print(i)



# while loop ----->

# The sum of first n numbers

# n = int(input('Enter a number: '))
# s=0
# i=1
# while i <= n:
#     s = s+i
#     i+=1
# print('The Sum: ', s)

# sum = (n*(n+1))/2
# print(sum)
    


# Some name from the Keyboard
# if the name is Anurag....if the name is not Anurag

# name = ''
# pwd=''
# while name!='Anurag' or pwd!='python':
#     name=input('Enter Name: ')
#     pwd=input('Enter pwd: ')
# print('Confirm!!!')




# Infinite loop ----->

# i = 0
# while True:
#     i += 1
#     print('Hello', i)
 



# Nested loops ----->

# for i in range(4):
#     for j in range(4):
#         print('i={} and j={}'.format(i, j), end=', ')
#         # print(f'i={i} and j={j}')


# the number of rows: 3
# *
# **
# ***
# https://pynative.com/print-pattern-python-examples/
#-----------------------------
# n = int(input('-->'))
# for i in range(1,n+1):
#     print('*'*i,)
#-----------------------------
# n = int(input('-->'))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print('*', end=' ')
#     print()
#-----------------------------
# n = int(input('--->'))
# for i in range( n):
#     print('* '*n)
#-----------------------------
# n = int(input('--->'))
# for i in range(n):
#     for j in range(n):
#         print('*', end='')
#     print()
#-----------------------------
# n = int(input('-->'))
# for i in range(1,n+1):
#     print('*'*i,)
#-----------------------------
# n = int(input('-->'))
# for i in range(1,n+1):
#     for j in range(i):
#         print('*'*i)
#     print()
#-----------------------------
# rows = 8
# # rows = int(input("Enter the number of rows "))
# for i in range(1, rows + 1):
#     for j in range(1, i + 1):
#         # multiplication current column and row
#         square = i * j
#         print(i * j, end='  ')
#     print()
#-----------------------------
rows = 5
k = 2 * rows - 2
for i in range(rows, -1, -1):
    for j in range(k, 0, -1):
        print(end=" ")
    k = k + 1
    for j in range(0, i + 1):
        print("*", end=" ")
    print("")
