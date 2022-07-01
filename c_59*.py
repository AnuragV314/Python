# ****   Pickling and unpickling of objects   ****:
# -------------------------------------------------
#Examples-->

#--->
# import pickle

# class Employee:
#     def __init__(self, eno, ename, esal, eaddr):
#         self.eno = eno
#         self.ename = ename
#         self.esal = esal
#         self.eaddr = eaddr

#     def display(self):
#         print(self.eno, '\t', self.ename, '\t', self.esal, '\t', self.eaddr, )    

# with open('emp.dat', 'wb') as f:
#     e = Employee('100', 'Anurag', 5000, 'UP')
#     pickle.dump(e, f)
#     print('Pickling of Employee object completed...')


# with open('emp.dat', 'rb') as f:
#     obj = pickle.load(f)
#     print('Employee Information afer unpickling...')
#     obj.display()



#--->

import pickle, emp59

f = open('emp.dat', 'wb')
n = int(input('Enter Number of Employee: '))

for i in range(n):
    eno = int(input('Enter Employee Number: '))
    ename = input('Enter Employee Name: ')
    esal = float(input('Enter Employee Salary: '))
    eaddr = input('Enter Employee Address: ')
    e = emp59.Employee(eno, ename, esal, eaddr)
    pickle.dump(e, f)

print('Pickling of Employee object completed...')
print()



# unpickling in other file  --> unpick.py





