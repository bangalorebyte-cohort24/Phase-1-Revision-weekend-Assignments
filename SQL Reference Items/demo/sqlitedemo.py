import sqlite3
conn = sqlite3.connect('employee.db')
c = conn.cursor()
# c.execute("""CREATE TABLE employees (
# 	First text,
# 	Last text,
# 	pay integer
# 	)""")
c.execute("INSERT into employees VALUES ('Jithin','J Kumar','10000')")
conn.commit()
c.execute("INSERT into employees VALUES ('Arun','J Kumar','20000')")
c.execute("SELECT * from employees WHERE Last ='J Kumar'")
print(c.fetchall())
conn.commit()
conn.close()
