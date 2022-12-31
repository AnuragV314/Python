# -------------------------------------------------------------
#       <-------------- REGULAR EXPRESSIONS -------------->
# -------------------------------------------------------------


# re module:
# --------------

# 1. compile() function:
# ------------------------
# import re
# pattern = re.compile('Python')
# print(type(pattern))

# 2. finditer():
# --------------
# matcher = pattern.finditer('Learinig Pyhton is very easy..')
 
# 3. start():
# -----------
# 4. end():
# ---------
# 5. group():
# -----------



# import re 

# count = 0
# pattern = re.compile('ab')
# matcher = pattern.finditer('ababaaba')
# for match in matcher:
#     count += 1
#     print('match is available at start index: ', match.start())

# print('The number of accurrences is: ', count)



# 
# import re
# count = 0
# pattern = re.compile('ab')
# matcher = pattern.finditer('abaabaabaa')

# for match in matcher:
#     count += 1 
#     print(f'start: {match.start()}, end: {match.end()}, group:{match.group()}')

# print('The number of accurrences is: ', count)


# 
# import re
# count = 0
# matcher = re.finditer('ab', 'abaabaabaa')
  
# for match in matcher:
#     count += 1 
#     print(f'start: {match.start()}, end: {match.end()}, group:{match.group()}')

# print('The number of accurrences is: ', count)
# ---------------------------------------------

 


# Character classes:(NOTES) 
# -----------------------------------

# import re
# matcher = re.finditer('[^a-zA-Z0-9]', 'a7b@k9z')
# for m in matcher:
#     print(m.start(), '....', m.group() )



# Predefined Character classes:(NOTES) 
# ------------------------------------

# import re
# matcher = re.finditer('.', 'a7b @k9z')
# for m in matcher:
#     print(m.start(), '....', m.group() )



# Quantifiers:(NOTES)
# -------------------

# import re
# matcher = re.finditer('^a', 'abaabaabaaab')
# for m in matcher:
#     print(m.start(), '....', m.group() )
# ----------------------------------------------


# Important functions of 're' module:
# ------------------------------------
# 1. match()
# 2. fullmatch()
# 3. search()
# 4. findall()
# 5. finditer()
# 6. sub()
# 7. subn()
# 8. split()
# 9. compile()


# 1. match():
# -----------
# import re
# s = input('Enter pattern to check: ')
# m = re.match(s, 'abcdefgh')
# if m!=None:
#     print('Match is availble at the beginning of the string')
#     print(f'start index: {m.start()} and end index: {m.end()}')
# else:
#     print('Match is not availble at the beginning of the string')


# 2. fullmatch():
# ---------------
# import re
# s = input('Enter pattern to check: ')
# m = re.match(s, 'abcdefgh')
# if m!=None:
#     print('Full String Match')
# else:
#     print('Full String Not Match')


# 3. search():
# ------------
# import re
# s = input('Enter pattern to check: ')
# m = re.search(s, 'abaabaaab')
# if m!=None:
#     print('Match is available')
#     print(f'start index: {m.start()}, end index: {m.end()}')
# else:
#     print('Match is not available')


# 4. findall():
# ------------
# import re
# l = re.findall('[0-9]', 'a7b9k6z')
# print(l)









