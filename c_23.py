#Mathematical operators: ---> (+  *)

# s[:]---->forward direction
# s[::-1]---->backward direction

# Q. WAP to access each character of string in forward direction and backward direction?

# s = 'anurag'
# print(s[:])
# print(s[::-1])

# n = len(s)
# i=0
# print('Data In Forward Direction')
# while i<n:
#     print(s[i], end='')
#     i+=1

# print('\nData In Backward Direction')
# i=-1
# while i>= -n:
#     print(s[i], end='')
#     i-= 1


# Q1. remove the duplicate characters from the string
# Q2. each character how many time presenting
# Q3. Durga Software Solution
        # reverse: urgaD oftwareS olutionS



#Membership operators: ---> (in,  not in)

# s= input('Enter Main String: ')
# subs = input('Enter Substring to Search : ')

# if subs in s:
#     print(subs, 'is found in Main String')
# else:
#     print(subs, 'is not found in Main String')



city = input('Enter Your City Name: ').strip()
list = ['Hyderabad', 'Delhi', 'Mumbai', 'Bangalore']

if city in list:
    print('Your City is available and CCC are XXX')
else:
    print(city, 'Not available...Plz enter a valid city name')

