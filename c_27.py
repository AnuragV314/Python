# Q1.
# Somthig:
# even index
# odd index

# Q2.
# s1 = 'RAVI'
# s2 = 'TEJA'
# output: RTAEVJIA

# Q3.
# input:B4A1D3
# output: ABD, 134

# Q4. 
# input:a4b3c2
# output:aaaabbbcc

# Q5. 
# input:a4k3b2
# output:aeknbd



#1.
# s = input('Enter somthing')
# print(s[1::2])
# print(s[::2])

# i = 0
# print('Even Position:------> ')
# while i < len(s):
#     print(s[i], end=',')
#     i+=2

# j = 1
# print('\nOdd Position:------> ')
# while j < len(s):
#     print(s[j], end=',')
#     j+=2


#3.
# s = input('Enter somthing: ')
# s1=s2=output= ''

# for x in s:
#     if x.isalpha():
#         s1 = s1+x
#     else:
#         s2=s2+x    

# for x in sorted(s1):
#     output=output+x  

# for x in sorted(s2):
#     output=output+x  

# # print(s1)
# # print(s2)
# print(output)


#4.
# s = input('Enter some string: ')
# output = ''

# for x in s:
#     if x.isalpha():
#         output = output+x
#         previous = x
#     else:
#         output = output+previous*(int(x)-1)

# print(output)

#5.
# chr(unicode) ====> character
# ord(char) =======> unicode
# >>> chr(65) ---->'A'
# >>> ord('a') ----->97


# s = input('Enter some string: ')
# output = ''
# for x in s:
#     if x.isalpha():
#         output += x
#         previous = x
#     else:
#         newch=chr(ord(previous)+int(x))
#         output += newch
# print(output)

# 2.
# s1 = input('Enter first string: ')
# s2 = input('Enter second string: ')

#for same string
# output=''
# i=j=0
# while i<len(s1) or j <len(s2):
#     output += s1[i]+s2[j]
#     i += 1
#     j += 1
# print(output)

#  for different string
# output=''
# i=j=0
# while i<len(s1) or j <len(s2):
#     if i<len(s1):
#         output += s1[i]
#         i += 1
#     if j<len(s2):
#         output += s2[j]
#         j += 1
# print(output)

# -------------------------------

# Q. To remove duplicates presetnt in string:

# s= 'fdgfgfghhh'
# l = []
# for x in s :
#     if x not in l:
#         l.append(x)
# output = ''.join(l)
# print(output)

#or
# print(''.join(set(s)))


# Q. Find the number of accurrences of each character:

# d = {100:'d', 34:'r'}
# for k,v in d.items():
#     print('{}:{}'.format(k,v))


s = input('some string: ')
d = {}
for x in s:
    if x not in d.keys():
        d[x]=1
    else:
        d[x] = d[x]+1    
# print(d)
for k,v in d.items():
    print('{} occurrs {} times'.format(k,v))







