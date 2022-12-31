# Import Function/Method for set:
#---------------------------------
# 1. add()----> s.add(new element)
# 2. update() -----> s.update(x,y,z)  (x,y,z =====>list,tuple,element, etc)
# 3. copy()
# 4. pop()
# 5. remove(x)
# 6. discard(x) ---> not give error
# 7. clear() ----> remove all element
# -----------------------------------------------------------------


# Import Function/Method for set:
#---------------------------------
# 1. union()-----> s1.union(s2) or s1|s2
# 2. intersection()-----> s1.intersection(s2) or s1&s2
# 3. difference()-----> s1.difference(s2) or s1-s2
# 4. ....
# ------------------------------------------------------------------


# Set comprehension
# ----------------------------
# s = {expression for i in sequence if condition}



# ------------------------------------------------
# Q. To eliminate duplicate present in the list?
# l = (12,34,12,56,12,45,45,34,56)
# # s = set(l)
# # print(list(s))

# l1 = []
# for x in l:
#     if x not in l1:
#         l1.append(x)
# print(l1)
# -----------------------------------------------

# w = input('Enter some word: ')
# s = set(w)
# v = {'a','e','i','o','u'}
# d = s.intersection(v)
# print('Vowels: ', d)

# -------------------------------------------------



# -----------------------------------------------------------
#                       Dictionary Data Structure
# -----------------------------------------------------------

# d = {}
# d[100] = 'anurag'
# d[200] = 'shanu'
# d['drama'] = 'nice'
# print(d) #{100: 'anurag', 200: 'shanu', 'drama': 'nice'}

# Q.---->(notes)

rec = {}
n = int(input('Enter number of student: '))
i = 1
while i <= n:
    name = input('Enter the name: ')
    marks = input('Enter % of marks: ')
    rec[name]=marks
    i += 1

print('Name of Student', '\t', '% of Marks')
for x in rec:
    print('\t', x, '\t\t', rec[x])

