import os
import pytils
import sqlite3
import calendar
import datetime
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import datetime
import pytils
# from .models import People
# from .models import Static


import sqlite3
import hashlib
import logging
from collections import OrderedDict

peoples = [
    ['Белкин', 'C3888', '172.41.0.129', '0c60055f2b435aca204a82987580290ff7bff461'],
    ['Середа', 'C3535', '172.41.0.130', 'eb2cc1603e8d22f1f3d6de51f7ca84799fe75623'],
    ['Бунакова', 'C3537', '172.41.0.131', '1f81c91f6c272b317fa3db9630f3603a221af664'],
    ['Чуркина', 'C3251', '172.41.0.133', 'c375bd242b60423ef8e5902fbc3eb7864610d1c2'],
    ['Бирюкова', 'C3887', '172.41.0.134', '2d5c6ca982ccb2038e68389cdf563130162e82d3'],
    ['Изыльметьева', 'C3889', '172.41.0.137', 'fbd090252878d2a8ec29a0e22d0e807874f6cafc'],
    ['Серкова', 'C3886', '172.41.0.138', 'f06b8537ddbce7d01453423d239f4e909261b2cd'],
    ['Антипин', 'C3540', '172.41.0.139', '16222ebeb801394cb869ec860cb48e3c80b1ce06'],
    ['Семякина', 'C2652', '172.41.0.140', '4cd574116138ffc20467884ca440968c3599835e'],
    ['--Соколов', 'C2972', '172.41.0.141', '58de5afa48ce82ba1afd2bb63e8fc0123a9fb175'],
    ['Коршунова', 'C3221', '172.41.0.142', 'dd9578434e440de8abf0d6fad9404cd041c0a624'],
    ['Выборнова', 'C2860', '172.41.0.144', 'eaf2037d5253f0fa204aa1e73356c38bb1a45a8b'],
    ['Дубровина', 'C2654', '172.41.0.145', 'e8cce07cf8a369784ac600264fac0d36bc115404'],
    ['Борщева', 'C3891', '172.41.0.147', 'ffa0892e921deaf50921ec608f8af8f7e949ea48'],
    ['Сахно', 'C2655', '172.41.0.149', '003d89eab2525dc7ae311848c51815f47aae0e28'],
    ['Сосина', 'C3893', '172.41.0.152', 'b4e4d51fc3efcdeacc8ab3507419885bc2c87097'],
    ['--Рябин', 'C2859', '172.41.0.153', '686e5ddf657ad05cc77de9265f35d6195ed6874a'],
    ['Смирнов', 'C3246', '172.41.0.154', '1006786b03dc970475ea60984eb8d59f957d5c04'],
    ['Поликарпов', 'C3230', '172.41.0.159', '79c411e3d71ac036987015c8bf549cc65e1c9e93'],
    ['Пономарева', 'C2973', '172.41.0.161', 'f464d6f0d3c5949d648e1dab3d46b97497f57fdf'],
    ['Пирогов', 'C3884', '172.41.0.163', '17e0564293cc0dfc778b5828ab9948dcfa1f021a'],
    ['Баранчугова', 'C3890', '172.41.0.164', '0dc2ee16a2118c9105eb3ae73abcc7765bb4de7b'],
    ['Сканер', 'C3236', '172.41.0.165', 'fd35e934d94661acef652a8d9544e7db4d94febc'],
    ['Соколов', 'C3539', '172.41.0.166', 'cdafef5054246f7e5fd02ede9bf04b5951efadbc'],
    ['Рябин', 'C3892', '172.41.0.167', '6304f214eaded0d08587605fc31b30aee9393aa2'],
    ['Лаптенок', 'C3885', '172.41.0.168', 'eba535dcde4b3049c13041361ed77c8dcbe93dc3'],
    ['Апполонова', 'C3541', '172.41.0.169', '349d28dc2118d5a6689324c754c03ed8b9952568'],
    ['Смекалина', 'C3534', '172.41.0.170', '9cd871a1d21123a86f9d4ea673a0bf904e49c93d'],
    ['Вешонкина', 'C3536', '172.41.0.171', '6cbacff29b8c57562056e6254be29ac697f577bb'],
    ['Кузнецова', 'C4509', '172.41.0.172', '87ee65f7072877a68ce5a4dc987e88e5004720cb'],
    ['Скрипкин', 'C4512', '172.41.0.173', '42156231f7e40be652043419dd81e41eb35a6e3a'],
    ['Тихоненок', 'C4515', '172.41.0.174', '0584d35887d1eb985941b1bf97571ba51d245e0e'],
    ['Гелеверя', 'C4517', '172.41.0.175', '9cff70cdc998940a4be059ef12766272311768f6'],
    ['Тарынина', 'C4511', '172.41.0.176', 'a8594d106e2520294796de56458185d777e6e56f'],
    ['Салимов', 'C4510', '172.41.0.177', 'cbfde08b5e3da211fb90d6a7e8ef40a48ee4a2e0'],
    ['Алексеева', 'C4513', '172.41.0.178', 'e6d0f4bd11fb1f0047e8a582e38dac16f0836ea9'],
    ['Каширский', 'C4506', '172.41.0.179', 'b654bb5521482dfc5bca4266636992aab4a1fb91'],
    ['Задонская', 'C2653', '172.41.0.181', '9f0faabedce891e8f1d34a8ce7416c7755beb125'],
    ['Муллагалеева', 'C4514', '172.41.0.183', 'cda52c9bb256a606cdc4cb33e4c686400ae74119'],
    ['Кожевников', 'C4507', '172.41.0.184', 'c7d80ab030202cb59775efdc768fecaced54fcb3'],
    ['Темиргалеев', 'C4516', '172.41.0.188', '74620af4882e8e7244daf1060d99d29fda2cb1fe'],
    ['Шемякин', 'C4508', '172.41.0.192', '4a5c29a93c085b7eea81c3a2d6d911e5ca791f1b'],
    ['MacBook VPN', 'home', '10.0.0.5', '00d735369988d4bbd0d404a166a6f8b871027763'],
    ['Kodachi VPN', 'home', '10.0.0.3', 'd854e2039a3e27436167f5e1bd2b0544a1fddd7d'],
    ['localhost', 'localhost', '127.0.0.1', '4b84b15bff6ee5796152495a230e45e3d7e947d9'],
    ['MacBook', 'home', '192.168.88.253', 'a7f5f7e93e89ff3d2b8e5d0dec876268e74c038c'],
    ['Kodachi', 'home', '192.168.88.227', '6875936c22ff4e8ccb6da5ddba4ba22667bdb08c'],
    ['Хомяков', 'C3538', '172.41.0.132',  '1680050e21c86c6a256aa275232ff13a2f6bfe0e'],

]


# os.chdir('../')
# from .models import People
conn = sqlite3.connect(r'../db.sqlite3')
cur = conn.cursor()
cur.execute("SELECT * FROM duty_people")
one_result = cur.fetchone()
# print(one_result)
new_results = []
print('читаем базу данных')
cur.execute("SELECT * FROM duty_people;")
all_results = cur.fetchall()
for i, a_r in enumerate(all_results):
    # print(f'{a_r = }')
    if a_r[5] == '0.0.0.0':
        # print(f'{a_r[1] = }')
        # print(f'{a_r[5] = }')
        for id in peoples:
            # print(f'{id = }')
            if id[0] == a_r[1]:
                new_results.append([
                    all_results[i][0],
                    all_results[i][1],
                    all_results[i][2],
                    all_results[i][3],
                    id[3],
                    id[2],
                ])
    else:
        new_results.append([
            all_results[i]
        ])
    # print(f'{new_results[i] = }')
for i, a_r in enumerate(new_results):
    print(f'{i+1}) {a_r}')

conn.close()

#
# print('добавляем в базу данных')
#
#
# cur.execute("""INSERT INTO duty_people(id, familia, imya, otche)
#    VALUES('5', 'Alex', 'Smith', 'male');""")
#
# user = ['6', 'qqq', 'www', 'eee']
# cur.execute("INSERT INTO duty_people VALUES(?, ?, ?, ?);", user)
#
# more_users = [['7', 'Peter', 'Parker', 'Male'],
#               ['8', 'Bruce', 'Wayne', 'male']]
# cur.executemany("INSERT INTO duty_people VALUES(?, ?, ?, ?);", more_users)
#
# print('читаем базу данных')
# cur.execute("SELECT * FROM duty_people;")
# all_results = cur.fetchall()
# for a_r in all_results:
#     print(a_r)
# print(len(all_results))
#
#
# print('удаляем лишнее')
# for i in range(5, (len(all_results)+2)):
#     cur.execute(f"DELETE FROM duty_people WHERE id='{i}';")
#
#
# print('читаем базу данных')
# cur.execute("SELECT * FROM duty_people;")
# all_results = cur.fetchall()
# print(len(all_results))
# for a_r in all_results:
#     print(a_r)
# conn.commit()



# c = calendar.Calendar()
# today = datetime.datetime.now()
# god, mes = today.year, today.month
# now = pytils.dt.ru_strftime(u"%d - %a", inflected=True, date=today)
# # now = pytils.dt.ru_strftime(u"сегодня - %d %B %Y, %A", inflected=True, date=today)
# table = []
# id = []
# chislo = []
# den_ned = []
# pers_id = 1
# supe_id = 1
# da_of_we = []


#
#
# for i in c.itermonthdays(god, mes):
#     stro = []
#     if i != 0:
#         day = datetime.date(god, mes, i)
#         dayy = str(day)
#         # dayy = pytils.dt.ru_strftime(u"%D", inflected=True, date=day)
#         n_d = calendar.weekday(god, mes, i)
#         stroka = pytils.dt.ru_strftime(u"%Y-%B-%D", inflected=True, date=day)
#
#         day_of_week  = pytils.dt.ru_strftime(u"%a", inflected=True, date=day)
#         if n_d in range(5):
#             # id.append(i)
#             # chislo.append(day)
#             # da_of_we.append(day_of_week)
#             stro.append(i)
#             stro.append(dayy)
#             stro.append(day_of_week)
#             stro.append(36)
#             stro.append(1)
#             stro.append(1)
#             table.append(stro)
#
#         elif n_d == 5:
#             pass
#
# for t in table:
#     print(t)
#
#





# print('читаем базу данных')
# cur.execute("SELECT * FROM duty_people;")
# all_results = cur.fetchall()
# for a_r in all_results:
#     print(a_r)

# print('удаляем лишнее')
# for i in range(0, (len(all_results))):
#     cur.execute(f"DELETE FROM duty_month WHERE id='{i}';")
# print('читаем базу данных')
# cur.execute("SELECT * FROM duty_month;")
# all_results = cur.fetchall()
# for a_r in all_results:
#     print(a_r)
peoples_ip = OrderedDict()
peoples_hash = OrderedDict()

# for id, familia, imya, otche, hash, ip in all_results:
#     peoples_ip[familia] = ip
#     peoples_hash[familia] = hash
#     print(f'{peoples_ip[familia] = } - {peoples_hash[familia] = }')
# cur.executemany("INSERT INTO duty_month VALUES(?, ?, ?, ?, ?, ?);", table)
# conn.commit()
# conn.close()

# imena = People.objects.in_bulk()

# print(f'{imena = }')