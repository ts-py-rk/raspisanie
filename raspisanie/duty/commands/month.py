import sqlite3
import os

os.chdir('../')
os.chdir('../')

conn = sqlite3.connect(r'db.sqlite3')
cur = conn.cursor()
# cur.execute("SELECT * FROM duty_people")
# one_result = cur.fetchone()
# print(one_result)

print('читаем базу данных')
cur.execute("SELECT * FROM duty_people;")
all_results = cur.fetchall()
for a_r in all_results:
    print(a_r)

print('добавляем в базу данных')


cur.execute("""INSERT INTO duty_people(id, familia, imya, otche)
   VALUES('5', 'Alex', 'Smith', 'male');""")

user = ['6', 'qqq', 'www', 'eee']
cur.execute("INSERT INTO duty_people VALUES(?, ?, ?, ?);", user)

more_users = [['7', 'Peter', 'Parker', 'Male'],
              ['8', 'Bruce', 'Wayne', 'male']]
cur.executemany("INSERT INTO duty_people VALUES(?, ?, ?, ?);", more_users)

print('читаем базу данных')
cur.execute("SELECT * FROM duty_people;")
all_results = cur.fetchall()
for a_r in all_results:
    print(a_r)
print(len(all_results))


print('удаляем лишнее')
for i in range(5, (len(all_results)+2)):
    cur.execute(f"DELETE FROM duty_people WHERE id='{i}';")


print('читаем базу данных')
cur.execute("SELECT * FROM duty_people;")
all_results = cur.fetchall()
print(len(all_results))
for a_r in all_results:
    print(a_r)
conn.commit()

print('читаем базу данных')
cur.execute("SELECT * FROM duty_month;")
all_results = cur.fetchall()
for a_r in all_results:
    print(a_r)


conn.close()