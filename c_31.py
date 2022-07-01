# Comparing List object:
# ----------------------------

# x = ['Dog', 'Cat', 'Rat']
# y = ['Dog', 'Cat', 'Rat']
# z = ['DOG', 'CAT', 'RAT']

# print(x==y)
# print(x==z)
# print(x!=z)


# x = [50, 20, 30]
# y = [50, 90, 100, 120, 170]
# print(x>y) 
# print(x>=y)
# print(x<=y)



# clear():
# ---------------------------
# x = [10,20,30]
# print(x)
# x.clear()
# print(x)


# Nested Lists:
# ---------------------------

# x = [[10,20,30], [40,50,60], [70,80,90]]
# print(x)
# print('Elements row wise: ')
# for r in x:
#     print(r)

# col = int(input('which column(1-3): '))
# for i in range(len(x)):
#     print(x[i][col-1])

# print('Elements in Matrix Style: ')
# for i in range(len(x)):
#     for j in range(len(x[i])):
#         print(x[i][j], end=' ')
#     print()    



# List Comprehensions: ---> [expression for i in sequence]
#                           [expression for i in sequence if condition]
# -------------------------------------------

                # l = [1,4,9,16,25,36....]
                # l = []
                # for i in range(11):
                #     l.append(i**2)
                # print(l)
                # # or
                # for i in range(11):
                #     print(i**2, end=' ')

# ---->

# l = [i**2 for i in range(11)]
# print(l) 

# l = [2**i for i in range(1,11)]
# print(l)


# n1 = [10,20,30,40]
# n2 = [30,40,50,60]
# n3 = [x for x in n1 if x not in n2]
# print(n3)


words = "the quick brown fox jumps over the lazy dog".split()
print(words)

l = [[w.upper(), len(w)] for w in words]
print(l)



