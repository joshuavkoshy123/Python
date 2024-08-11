import sqlite3
 
conn = sqlite3.connect('test.db')
print ("Opened database successfully")
conn.execute("UPDATE COMPANY set NAME = 'Justin' where ID=2")
conn.execute("UPDATE COMPANY set SALARY = 100000 where ID=2")
conn.execute("UPDATE COMPANY set SALARY = 150000 where ID=1")
conn.execute("UPDATE COMPANY set ADDRESS = 'Arizona' where ID=3")
conn.execute("UPDATE COMPANY set SALARY = 90000 where ID=3")
conn.execute("UPDATE COMPANY set ADDRESS = 'Minnesota' where ID=4")
conn.execute("UPDATE COMPANY set SALARY = 80000 where ID=4")
conn.commit()
print ("Total number of rows updated :", conn.total_changes)
cursor = conn.execute("SELECT id, name, age, address, salary from COMPANY")
for row in cursor:
    print ("ID = ", row[0])
    print ("NAME = ", row[1])
    print ("AGE = ", row[2])
    print ("ADDRESS = ", row[3])
    print ("SALARY = ", row[4], "\n")
    print ("Operation done successfully")
conn.close()


