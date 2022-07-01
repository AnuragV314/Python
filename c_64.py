# class Test:
#     x = 10
#     def __init__(self):
#         self.y = 20

# t1 = Test()
# t2 = Test()

# t1.x = t1.x + 1
# t2.y = t2.y + 1
# print('t1: ', t1.x, t1.y)
# print('t2: ', t2.x, t2.y)
# print('Test: ', Test.x)


# class Test:
#     a=10
#     def __init__(self):
#         self.b = 20

# t1 = Test()
# t2 = Test()
# Test.a = 888
# t1.b = 999
# print('t1: ', t1.a, t1.b)
# print('t2: ', t2.a, t2.b)



# class Test:
#     a=10
#     def __init__(self):
#         self.b = 20
#     def m1(self):
#         self.a = 888
#         self.b=999

# t1 = Test()
# t2 = Test()
# t1.m1()
# print('t1: ', t1.a, t1.b)
# print('t2: ', t2.a, t2.b) 



# class Test:
#     a=10
#     def __init__(self):
#         self.b = 20
#     @classmethod    
#     def m1(cls):
#         cls.a = 888
#         cls.b=999

# t1 = Test()
# t2 = Test()
# t1.m1()
# print('t1: ', t1.a, t1.b) 
# print('t2: ', t2.a, t2.b)
# print(Test.a, Test.b)



# How to delete static variable of a class?:
# ------------------------------------------

# class Test:
#     a= 10
#     def __init__(self) :
#         del self.a
#     @classmethod
#     def m1(cls):
#         del cls.a

# Test.m1()
# print(Test.__dict__)

# t = Test() # error
# del t.a # error



#ex
import sys
class Customer:
    '''Customer class with bank operation'''
    bankname = 'DURGABANK'
    def __init__(self, name, balance=0.0):
        self.name = name
        self.balance = balance
    def deposit(self, amt):
        self.balance = self.balance + amt 
        print('Balance after deposit: ', self.balance)
    def withdraw(self, amt):
        if amt>self.balance:
            print('Insufficient Fund.. cannot perform this operation.')
            sys.exit()
        self.balance = self.balance - amt 
        print('Balance after withdraw: ', self.balance)    


print('Welcome to', Customer.bankname)       
name = input('Enter your name: ')
c = Customer(name)

while True:
    print('d-Deposit \nw-Withdraw \ne-exit')
    option = input('Chose your option: ')
    if option=='d'or option=='D':
        amt=float(input('Enter ampunt: '))
        c.deposit(amt)
    elif  option=='w'or option=='W':
        amt=float(input('Enter ampunt: '))
        c.withdraw(amt)
    elif  option=='e'or option=='E':
        print('Thanks for banking', c.name)   
        sys.exit()
    else:    
        print('Invalid option...Plz choose valid option')
        
