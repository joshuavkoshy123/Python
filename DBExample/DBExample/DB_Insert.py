import sqlite3
conn = sqlite3.connect('test.db')
print ("Opened database successfully")
conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (5, 'Joseph', 40, 'Texas', 100000.00 )")
conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
VALUES (6, 'Josiah', 21, 'Florida', 85000.00 )")
conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
VALUES (7, 'Adrian', 24, 'Nebraska', 95000.00 )")
conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
VALUES (8, 'Matthew', 29, 'New York', 110000.00 )")
conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (9, 'Alex', 25, 'California', 120000.00 )")
conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
VALUES (10, 'Janice', 22, 'South Dakota', 85000.00 )")
conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
VALUES (11, 'Jennifer', 30, 'Georgia', 95000.00 )")
conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
VALUES (12, 'Aurora', 26, 'California', 110000.00 )")
conn.commit()
print ("Records created successfully")
conn.close()