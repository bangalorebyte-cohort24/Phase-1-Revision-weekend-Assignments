#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('test_again.db')
print ("Opened database successfully")

conn.execute("UPDATE COMPANY set SALARY = 25000.00 where AGE >= 25")
conn.commit()
print ("Total number of rows updated :", conn.total_changes)



#cursor = conn.execute("SELECT id, name, address, salary from COMPANY WHERE SALARY >= 10000 AND AGE >=25")
#cursor = conn.execute("SELECT id, name, address, salary from COMPANY WHERE SALARY >= 10000 OR AGE >=25")

cursor = conn.execute("SELECT id, name, address, salary from COMPANY WHERE SALARY >= 10000")
for row in cursor:
   print ("ID = ", row[0])
   print ("NAME = ", row[1])
   print ("ADDRESS = ", row[2])
   print ("SALARY = ", row[3], "\n")

print ("Operation done successfully")

conn.close()