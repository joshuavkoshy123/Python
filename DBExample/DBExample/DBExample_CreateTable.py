import sqlite3

conn = sqlite3.connect('test.db')
print ("Opened database successfully")
conn.execute("Drop table COMPANY")
conn.execute('''CREATE TABLE if not exists COMPANY
(ID INT PRIMARY KEY NOT NULL,
NAME TEXT NOT NULL,
AGE INT NOT NULL,
ADDRESS CHAR(50),
SALARY REAL);''')
print ("Table created successfully")
conn.close()
