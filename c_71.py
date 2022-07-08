# 5. finditer():
# ---------------
# import re
# matcher = re.finditer('\D', 'a7bk9z6')
# for m in matcher:
#     print(m.start(), '....', m.group() )



# 6. sub():
# ---------
# import re
# s = re.sub('\d', 'xxxxx', 'a7b9k5t9k')
# print(s)



# 7. subn():
# ----------

# import re
# t = re.subn('\d', 'xxxxx', 'a7b9k5t9k')
# print(type(t))
# print('The Result String:', t[0])
# print('The number of replacement: ', t[1])



# 8. split():
# -----------
# import re

# l = re.split('-', '10-20-30-40-50')
# print(l)

# l = re.split('.', 'www.durgasoftvido.com') # . means everything 
# for x in l:
#     print(x)

# l = re.split('\.', 'www.durgasoftvido.com') # .
# for x in l:
#     print(x)

# l = re.split('[.]', 'www.durgasoftvido.com') # .
# for x in l:
#     print(x)


# --------------------------------------------------------------------
# --------------------------------------------------------------------



# ^ symbol :
# ---------
# import re
# s = 'Learning Python is very easy'

# res = re.search('^Learn', s)

# if res != None:
#     print('Target string starts with Learn')
# else:
#     print('Target string not starts with Learn')



# $ symbol:
# ---------
# import re
# s = 'Learning Python is very Easy'

# res = re.search('easy$', s, re.IGNORECASE)

# if res != None:
#     print('Target string ends with easy')
# else:
#     print('Target string not end with easy')



# ---------------------------------------------
# ---------------------------------------------

# ? write a RE to represent all YAVA Language Identifires:

# import re
# s = input('Enter Identifire to validate: ')
# m = re.fullmatch('[a-k][0369][a-zA-Z0-9#]*', s)
# if m != None:
#     print(s, 'is valid Yava Identifire')
# else:
#     print(s, 'is not valid Yava Identifire')

# --------------------------------


# ? 10 digit  mobile number:
# import re
# s = input('Enter Your Mobile Number : ')
# m = re.fullmatch('[6789][0-9]+8', s)
# if m != None:
#     print(s, 'valid Number')
# else:
#     print(s, 'not valid Number')


# import re
# s = input('Enter Your Mobile Number : ')
# m = re.fullmatch('[6789][0-9]{8,12}', s)
# if m != None:
#     print(s, 'valid Number')
# else:
#     print(s, 'not valid Number')

# ---------------------------------------


# ? WAPP to extract all the mobile number present in the input.txt file.

# import re
# f1 = open('input.txt', 'r')
# f2 = open('output.txt', 'w')

# for line in f1:
#     list = re.findall('[0-9]\d{9}', line)
#     for number in list:
#         f2.write(number+'\n')

# print('Extracted all mobile numbers into output.txt')
# f1.close()
# f2.close()

# -------------------------------------------------------------------






# ***************************************************************
# --------------------------------------
# Web Scraping by Regular Expressions ::
# --------------------------------------

# import re, urllib
# import urllib.request

# sites = ['https://www.google.com/', 'https://www.rediff.com/']

# for s in sites:
#     print('Searching....', s)
#     u = urllib.request.urlopen(s)
#     text = u.read()
#     title = re.findall('<title>.*</title>', str(text), re.IGNORECASE)
#     print(title[0])
    # print(text)




# ? Read all mobile number present in redbus.in
# ----------------------------------------------
# import re, urllib
# import urllib.request

# u = urllib.request.urlopen('https://www.redbus.in/info/contactus')
# text = u.read()
# numbers=re.findall('[0-9]{6}', str(text))

# for n in numbers:
#     print(n)



# ? mail id is valid gmail id or not:
# -----------------------------------

# import re

# s = input('Enter Your Email id: ')

# m = re.fullmatch('\w[a-zA-Z0-9_.]*@gmail[.]com', s)

# if m!=None:
#     print('Valid mail ID')
# else:
#     print('Invalid mail ID')




# ? Car registeration Number is valid TS number
# ----------------------------------------------
# import re

# s = input('Enter Car registeration Number: ')

# m = re.fullmatch('TS[012][0-9][A-Z]{2}\d{4}', s)

# if m!=None:
#     print('Valid registeration Number')
# else:
#     print('Invalid registeration Number')



# ? Check mobilee number:
# ---------------------------
# import re
# s = input('Enter you mobile number: ')
# m = re.fullmatch('(0|91|\+91)?[6789]\d{9}')
# if m!=None:
#     print('Valid mobile number')
# else:
#     print('Invalid mobile number')    




