import emp59, pickle

f = open('emp.dat', 'rb') 
print('Employee Information afer unpickling...')

while True:
    try:
        obj = pickle.load(f)
        obj.display()
    except EOFError :
        print('All Employees Completed')  
        break

f.close()
