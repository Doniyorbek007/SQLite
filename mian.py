import sqlite3

connect = sqlite3.connect("words.db")

cursor = connect.cursor()

# connect.execute('''
# CREATE TABLE INFO(
#          ID INT PRIMARY KEY     NOT NULL,
#          NAME           TEXT    NOT NULL,
#          AGE            INT     NOT NULL,
#          ADDRESS        CHAR(50),
#          SALARY         REAL);
#          ''')

Uzbek = input("UZ: ")
Russian = input("RU: ")
English = input("ENG: ")

connect.execute(f"INSERT INTO words_list (Uzbek,Russian,English) VALUES ('{Uzbek}','{Russian}','{English}');")

cursor.execute("SELECT * FROM words_list")

data = cursor.fetchall()

for i in data:
    print(i)


connect.commit()

print("Done!")

connect.close()