# Finding Sunbstring:-----> find(), index(), rfind(), rindex())

# s = 'anuragverma'
# print(s.find('rag'))
# print(s.find('zeeoo')) 

# s= 'learning pyhton is aaa very very easy!!!'
# print(s.find('pyhton'))

# s = 'anuragvermaanuragveram'
# print(s.find('a'))
# print(s.find('a', 5, 15))

# s = 'anuragvermaanuragveram'
# print(s.find('a', 5, 15))

#-----------------------------------


# s = input('Enter Main Sring: ')
# subs = input('Enter Subsring: ')
# try:
#     n=s.index(subs)
# except ValueError:
#     print('substing not found in the main string')
# else:
#     print('substing found')   


#-------------------------------------

# Q. WAP to display all the substring in the given main string?

s = input('Enter a string: ')
subs = input('Enter Substing: ')

flag = False
pos = -1
n = len(s)
count=0

while True:
    pos=s.find(subs, pos+1, n)
    if pos == -1:
        break
    else:
        print('Found at index: ',pos)
        flag = True
    count+=1    
if flag == False:
    print('Not found')
print('The number of accurrences: ', count)    


# count2 = s.count(subs,0,25)
# print(count2)
  


