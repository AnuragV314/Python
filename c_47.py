# import math 
# print(help(math))


# Random module:
# -------------- 
#                   to geneate random numbers
# -------------------------------------------

# import random
# print(dir(random))

'''
['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST', 
'SystemRandom', 'TWOPI', '_ONE', '_Sequence', '_Set', '__all__', '__builtins__', 
'__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', 
'__spec__', '_accumulate', '_acos', '_bisect', '_ceil', '_cos', '_e', '_exp', 
'_floor', '_index', '_inst', '_isfinite', '_log', '_os', '_pi', '_random', 
'_repeat', '_sha512', '_sin', '_sqrt', '_test', '_test_generator', '_urandom', 
'_warn', 'betavariate', 'choice', 'choices', 'expovariate', 'gammavariate', 'gauss', 
'getrandbits', 'getstate', 'lognormvariate', 'normalvariate', 'paretovariate', 'randbytes', 
'randint', 'random', 'randrange', 'sample', 'seed', 'setstate', 'shuffle', 'triangular', 'uniform', 
'vonmisesvariate', 'weibullvariate']
'''                                                                    

# 1. random():
# -----------
# from random import *

# for i in range(10):
#     print(random())


# 2. randint():
# --------------
# from random import *

# print(randint(1,100))


# 3. uniform():
# --------------
# from random import *

# print(uniform(1,10))


# 4. randrange(start, stop, step):
# --------------------------------
# from random import *

# for i in range(20):
#     print(randrange(10))


# 5. choice(): 
# ------------
# from random import *

# l = [1334,23434,3454,467,5676,634,7435,8435,945,4350]
# for i in range(10):
#     print(choice(l))


#Q1. WAP to find 6-digit random number as OTP

#Q2. To generate random pwd of 6 length 
#       1,3,5 are alphabet symble
#       2,4,6 are digits



from random import *

for i in range(10):
    print(chr(randint(65, 65+25)),randint(0,9),chr(randint(65, 65+25)),randint(0,9),chr(randint(65, 65+25)),randint(0,9), sep='')




