# a = input()


# a, b = [int(x) for x in input('Enter 2 Number : ').split()]
# print('The Product : ',a*b)

## Read 2 float values from the keyboard which are specify with , seperation and print sum

# a, b = [float(x) for x in input('Enter 2 Number : ').split(',')]
# print('The Sum :', a+b)

# a, b, c = [eval(x) for x in input('Enter 3 Number : ').split(',')]
# print(type(a), type(b), type(c))




# error
# a = eval(input('enter a str')) #give error
# print(type(a))


#Commond line Arguments ----> argv
from sys import argv
print(type(argv))

print(argv)
print(argv[1:])

