#      Abstraction
# ---------------------


# Abstract Method:
# ----------------

# from abc import *

# class Vahicle:
#     @abstractmethod
#     def getNoOfWheels(self):
#         pass



# class Fruit:
#     @abstractmethod
#     def teste(self):
#         pass



# Abstract class:
# ---------------

from abc import *

# class Vahicle(ABC):
#     @abstractmethod
#     def getNoOfWheels(self):
#         pass



# class Vahicle():
#     @abstractmethod
#     def getNoOfWheels(self):
#         print('Hello from abstract method')

# v = Vahicle() # it's possible
# v.getNoOfWheels()  




# class Vahicle(ABC):
#     @abstractmethod
#     def getNoOfWheels(self):
#         print('Hello from abstract method')

# v= Vahicle() # it's not possible




# class Vahicle(ABC):
#     @abstractmethod
#     def getNoOfWheels(self):
#         pass

# class Bus(Vahicle):pass
# b=Bus() # it's not possible



# class Vahicle(ABC):
#     @abstractmethod
#     def getNoOfWheels(self):
#         pass

# class Bus(Vahicle):
#     def getNoOfWheels(self):
#         return 7

# class Auto(Vahicle):
#     def getNoOfWheels(self):
#         return 3

# b=Bus() # it's possible
# print(b.getNoOfWheels())

# a=Auto() # it's possible
# print(a.getNoOfWheels())





# Interface :(not availble)
# ----------
# ----------




# class CollegeAutomation(ABC):
#     @abstractmethod
#     def m1(self): pass
#     @abstractmethod
#     def m2(self): pass
#     @abstractmethod    
#     def m3(self): pass

# class ImpCla(CollegeAutomation):
#     def m1(self):
#         print('m1 method implementation')

#     def m2(self):
#         print('m2 method implementation')

#     def m3(self):
#         print('m3 method implementation')    

# c = ImpCla()
# c.m1()
# c.m2()
# c.m3()




class CollegeAutomation(ABC):
    @abstractmethod
    def m1(self): pass
    @abstractmethod
    def m2(self): pass
    @abstractmethod    
    def m3(self): pass

class ImpCla(CollegeAutomation):
    def m1(self):
        print('m1 method implementation')

    def m2(self):
        print('m2 method implementation')

class ConcreateCls(ImpCla):
    def m3(self):
        print('m3 method implementation')    

c = ConcreateCls()
c.m1()
c.m2()
c.m3()