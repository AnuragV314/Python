# Traversing the elements of List:
# ------------------------------------
# 1. By using while loop:

# l = [1,2,3,4,5,64,53,645]
# i = 0
# while i<len(l):
#     print(l[i])
#     i +=1
  
# 1. By using for loop: 
# for i in l:
#     print(i)


# print only even number 

# for i in l:
#     if i%2 == 0:
#         print(i)
#     # else:
#     #     print('odd')    

# -------------------------------

# l = ['a','b','c','d','e','h','g']
# for i in range(len(l)):
#     print("'{}' is available at positive index {} and negetive index {}".format(l[i], i, i-len(l)))


# ---> To add all elements to list upto 100 which are divisible by 10
# l = []
# for i in range(101):
#     if i%10==0:
#         l.append(i)
# print(l)
# # or
# l = []
# for i in range(0, 101, 10):
#     l.append(i)
# # print(l)


# l.insert(1,34)
# l.insert(1324234,1000000)    
# print(l)

