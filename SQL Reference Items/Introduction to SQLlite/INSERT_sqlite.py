import sqlite3

conn = sqlite3.connect('test_again.db')
print ("Opened database successfully")

# insert command _ table name _ columns to insert into _ 
conn.execute("INSERT INTO COMPANY (NAME,AGE,ADDRESS,SALARY) \
      VALUES ('Paul', 32, 'California', 20000.00 )");

conn.execute("INSERT INTO COMPANY (NAME,AGE,ADDRESS,SALARY) \
      VALUES ('Allen', 25, 'Texas', 15000.00 )");

conn.execute("INSERT INTO COMPANY (NAME,AGE,ADDRESS,SALARY) \
      VALUES ('Teddy', 23, 'Norway', 20000.00 )");

conn.execute("INSERT INTO COMPANY (NAME,AGE,ADDRESS,SALARY) \
      VALUES ('Mark', 25, 'Rich-Mond ', 65000.00 )");

conn.execute("INSERT INTO DEPARTMENT (DEPT,EMP_ID)\
	  VALUES('Finance',9976)");

conn.execute("INSERT INTO DEPARTMENT (DEPT,EMP_ID)\
	  VALUES('HR',1100)");

conn.execute("INSERT INTO DEPARTMENT (DEPT,EMP_ID)\
	  VALUES('Business Development',7652)");

conn.execute("INSERT INTO DEPARTMENT (DEPT,EMP_ID)\
	  VALUES('Business Development',7120)");

conn.commit()
print ("Records created successfully")
conn.close()
