#Various possible combination of try-except-else-finally blocks:
# --------------------------------------------------------------
# 1.
# try:
#     print('try')

#2.
# except:
#     print('hello')


#3.
# else:
#     print('hello')


#4.
# finally:
#     print('hello')


#5.
# try:
#     print('hello')
# except:
#     print('except')


#6.
# try:
#     print('hello')
# finally:
#     print('finally')


#7.
# try:
#     print('hello')
# except:
#     print('except')    
# else:
#     print('else')

#8.
# try:
#     print('hello')   
# else:
#     print('else')


#9.
# try:
#     print('hello')   
# else:
#     print('else')
# finally:
#     print('finally')

 
#10.
# try:
#     print('hello') 
# except XXXX:
#     print('except')      
# except YYY:
#     print('except')


#11.
# try:
#     print('hello') 
# except:
#     print('except')      
# else:
#     print('else')
# else:
#     print('else')

#12.
# try:
#     print('hello') 
# except:
#     print('except')      
# finally:
#     print('finally')
# finally:
#     print('finally')


#13.
# try:
#     print('hello') 
# except:
#     print('except')      
# print('hello')
# except:
#     print('except')


#14.
# try:
#     print('hello') 
# except:
#     print('except')      
# print('hello')
# finally:
#     print('except')



#15.
# try:
#     print('hello') 
# except:
#     print('except')      
# print('hello')
# else:
#     print('except')


#16.
# try:
#     print('try') 
# except:
#     print('except')      
# try:
#     print('try')
# except:
#     print('except')

#17*.
# try:
#     print('try') 
# except:
#     print('except')      
# try:
#     print('try')
# finally:
#     print('finally')


#18.




# type of exceptions :
# --------------------
# 1. predifind exceptions/ InBuild exceptions
# 2. user defind exceptions/ customised exceptions

# 2.
# class classname:
#     def __init__(self, arg):
#         self.msg = arg 


class TooYoungExceptions(Exception):
    def __init__(self, arg):
        self.msg = arg


class TooOldExceptions(Exception):
    def __init__(self, arg):
        self.msg = arg

age = int(input('Enter age: '))

if age>60:
    raise TooYoungExceptions('Plz wait some more time definitely you get best match ')
elif age<18:
    raise TooOldExceptions('Your age already crossed marriage age  no chance of gatting marriage')
else:
    print('Thanks for registration....You will get match details by mail')




