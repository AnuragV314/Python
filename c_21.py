#------------------------------
# for i in range(100):
#     if i%10==0:
#         print(i)
#     else:
#         pass    
#------------------------------
# del: ------------>
#------------------------------
# x=10
# print(x)
# del x
# print(x)


# s = 'anurag' 
# del s[1]  # error

#------------------------------

#------------------------------
#------------------------------
#         STRING
#------------------------------
#------------------------------


# s = 'This is \' single quote symbol'
# s = '''This is ' single quote symbol'''

# s1 = 'This is \" double quote symbol'
# s1 = '''This is " double quote symbol'''

# s2 = 'This is \' and \" single double quote symbol'
# s2 = '''This is ' and " single double quote symbol'''

# print(s2)
#------------------------------
#------------------------------


#------------------------------
## How to access character of string

# 1.by using index
# s = 'anurag'
# print(s[0])

# 2. by using slice operetor ---> s[start:end:step]
# s = 'anurag'
# print(s[0:3])


s = 'anurag'
for i in range(len(s)):
    # print(f'The character at +ve index {i} and -ve index {-len(s)+i} is {s[i]}')
    # or
    print('The character at +ve index {} and -ve index {} is {}'.format(i, -len(s)+i, s[i]))

# for i in s:
#     print(i) 






