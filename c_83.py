#  <==: Working with Oracle Database :==>
# -----------------------------------------

import cx_Oracle
con=cx_Oracle.connect('scott/tiger@localhost')
if con!=None:
    print('Connected Successfully')
    print('Version: ', con.version)
else:
    print('Connection failed')








