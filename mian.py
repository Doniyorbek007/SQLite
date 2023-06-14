import sqlite3

connect = sqlite3.connect("workers.db")

cursor = connect.cursor()

# connect.execute('''
# CREATE TABLE INFO(
#          ID INT PRIMARY KEY     NOT NULL,
#          NAME           TEXT    NOT NULL,
#          AGE            INT     NOT NULL,
#          ADDRESS        CHAR(50),
#          SALARY         REAL);
#          ''')

connect.execute("INSERT INTO INFO (ID,NAME,AGE,ADDRESS,SALARY) \
VALUES (2, 'Jhone', 35, 'Texas', 10000.00 )");

connect.commit()
print("Done!")
connect.close()