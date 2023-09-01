import sqlite3

conn = sqlite3.connect('csea2.db')

cursor = conn.cursor()

table ="""CREATE TABLE STUDENTS( 

        URN INT PRIMARY KEY,
        Name VARCHAR(25), 
        Class VARCHAR(10),
        CRN INT

        );"""

cursor.execute(table)

cursor.execute('''INSERT INTO STUDENTS VALUES ('2104088', 'Deesha', 'CSE', '2115033')''')
cursor.execute('''INSERT INTO STUDENTS VALUES ('2104091', 'Dilpreet', 'CSE', '2115037')''')
cursor.execute('''INSERT INTO STUDENTS VALUES ('2104092', 'Dilram', 'CE', '2115038')''')
cursor.execute('''INSERT INTO STUDENTS VALUES ('2104093', 'Divneet', 'CSE', '2115039')''')
cursor.execute('''INSERT INTO STUDENTS VALUES ('2104096', 'Ekus', 'CSE', '2115043')''')
cursor.execute('''INSERT INTO STUDENTS VALUES ('2104100', 'Gundeep', 'CSE', '2115046')''')
cursor.execute('''INSERT INTO STUDENTS VALUES ('2104103', 'Gudrev', 'CSE', '2115049')''')
cursor.execute('''INSERT INTO STUDENTS VALUES ('2104113', 'Harnoor', 'CSE', '2115059')''')

# Commit your changes in the database	
conn.commit()

# Closing the connection
conn.close()
