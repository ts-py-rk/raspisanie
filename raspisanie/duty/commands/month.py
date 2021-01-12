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


import datetime
import calendar
import pytils

c = calendar.Calendar()
today = datetime.datetime.now()
god, mes = today.year, today.month
now = pytils.dt.ru_strftime(u"%d - %a", inflected=True, date=today)
# now = pytils.dt.ru_strftime(u"сегодня - %d %B %Y, %A", inflected=True, date=today)
table = []
id = []
chislo = []
den_ned = []
pers_id = 1
supe_id = 1
da_of_we = []




for i in c.itermonthdays(god, mes):
    stro = []
    if i != 0:
        day = datetime.date(god, mes, i)
        dayy = str(day)
        # dayy = pytils.dt.ru_strftime(u"%D", inflected=True, date=day)
        n_d = calendar.weekday(god, mes, i)
        stroka = pytils.dt.ru_strftime(u"%Y-%B-%D", inflected=True, date=day)

        day_of_week  = pytils.dt.ru_strftime(u"%a", inflected=True, date=day)
        if n_d in range(5):
            # id.append(i)
            # chislo.append(day)
            # da_of_we.append(day_of_week)
            stro.append(i)
            stro.append(dayy)
            stro.append(1)
            stro.append(1)
            stro.append(2)
            stro.append(day_of_week)
            table.append(stro)

        elif n_d == 5:
            pass

for t in table:
    print(t)







print('читаем базу данных')
cur.execute("SELECT * FROM duty_month;")
all_results = cur.fetchall()
for a_r in all_results:
    print(a_r)

cur.executemany("INSERT INTO duty_month VALUES(?, ?, ?, ?, ?, ?);", table)
conn.commit()


conn.close()