# 1. WAP to take dictionary from the keyboard and print the sum of values?

# d = eval(input('Enter Dictionary: '))
# sum_ = 0
# for x in d.values():
#     sum_ = sum_+x
# print(sum_)
# #or
# s = sum(d.values())
# print(s)



# 2. Number of occurrences of each letter present in the given string?

# s = input('Enter a string: ')
# d = {}
# for x in s:
#     d[x]=d.get(x, 0)+1
# for k,v in sorted(d.items()):   
#     print('{} occurred {} times'.format(k,v))


# 3. Number of occurrences of each vowels present in the given string?

# s = input('Enter a string: ')
# vowels = {'a','e','i','o','u'}
# d = {}
# for x in s:
#     if x in vowels:
#         d[x] = d.get(x, 0) + 1
# for k,v in sorted(d.items()):   
#     print('{} occurred {} times'.format(k,v))


# special---->

n = int(input('Enter the Number of students: '))
d = {}
for i in range(n):
    name = input('Enter Student Name: ')
    marks = input('Enter Student marks: ')
    d[name] = marks

while True:
    name = input('Enter Student Name to Get Marks: ')
    marks = d.get(name, -1)
    if marks == -1:
        print('Student Not Found')
    else:
        print('The marks of {} is {}'.format(name, marks))    

    option = input('Do you find another student marks [Yes|No]: ')
    if option=='No':
        break
print('Thanks for using our application')

 

 
   



