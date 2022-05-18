# # import datetime
# # import calendar
# # # from django.template.defaultfilters import date
# # # from django.utils.translation import get_language, activate
# # #
# # # today = datetime.datetime.now()
# # # # month = today.month
# # # # print (month)
# # # # print(today.strftime('%B'))
# # # # today = datetime.date.today()
# # # # # print(date(today, 'F'))
# # # # # month = calendar.month_name[1]
# # # # # print(month)
# # import pytils
# # # # b = pytils.numeral.get_plural(1, u"гвоздь, гвоздя, гвоздей")
# # # # print(b)
# # # # # c = pytils.dt.ru_strftime(u"сегодня - %d %B %Y, %A", inflected=True, date=datetime.date(2006, 9, 2))
# # # # c = pytils.dt.ru_strftime(u"сегодня - %d %B %Y, %A", inflected=True, date=today)
# # # day_of_week = pytils.dt.ru_strftime(u"%A", inflected=True, date=today)
# # # print(c)
# # # # # dow = datetime.datetime.weekday()
# # # # d_o_w = datetime.datetime.isoweekday(today)
# # # # # d_o_w = datetime.datetime.isoweekday(dow)
# # # # print(d_o_w)
# # #
# # #
# # # # mesyas = range(1,13)
# # # # for m in mesyas:
# # # #     # print(m)
# # # #     today = datetime.date(2020, m, 1)
# # # #     # print(f'{today.year} год, {today.month} месяц, {today.day} число')
# # # #     print(f'{pytils.dt.ru_strftime(u"сегодня  %a - %d %B %Y", inflected=True, date=today)}')
# # # #     # for d in today.day:
# # # #     #     print(d)
# # # # #
# # # # # print(today.year)
# # # # # mesyas = today.month
# # # # # # m = pytils.dt.ru_strftime(u'%B', date=mesyas)
# # # # # print(mesyas)
# # #
# # # # def date_iter(year, month):
# # # #     # cal = calendar.Calendar
# # # #     for i in range(1, calendar.monthrange(year, month)[0] + 1):
# # # #         yield date(year, month, i)
# # # #     # cal.itermonthdays(year, month)
# # # # #     # return cal.itermonthdates(calendar, month, year)
# # # # #
# # # # #
# # # # for d in date_iter(2019, 12):
# # # #     print(d)
# # # #
# # # # # print(date_iter(2019, 12))
# # #
# # # kalendar = calendar.Calendar(firstweekday=0)
# # # year = 2021
# # # month = 1
# # # test = calendar.monthrange(year, month)  # день недели первого дня месяца и количество дней в этом месяце
# # # print(test)
# # # # yanvar = calendar.itermonthday(year,month)
# # #
# # # # for i in yanvar:
# # # #     print(i)
# # #
# # # # for month in range (1, 13):
# # # #     macal = calendar.monthcalendar(2021, month)
# # # #     week1 = macal[0]
# # # #     week2 = macal[1]
# # # #
# # # #     if week1[calendar.MONDAY] != 0:
# # # #         auditday = week1[calendar.MONDAY]
# # # #     else:
# # # #         auditday = week2[calendar.MONDAY]
# # # #     print("%10s %2d" % (calendar.month_name[month], auditday))
# # #
# # # # import calendar
# # # # Создаем обычный текстовый календарь
# # # c = calendar.TextCalendar(calendar.THURSDAY)
# # # str = c.formatmonth(2025, 1, 0, 0)
# # # print (str)
# # # # перебираем через цикл дни месяца
# # # # нули указывают, что дни принадлежат смежному месяцу
# # # god = 2021
# # # mes = 1
# # # day_of_week = pytils.dt.ru_strftime(u"%A", inflected=True, date=today)
# # # for i in c.itermonthdays(god, mes):
# # #     if i != 0:
# # #         # print (f'{i} - {calendar.weekday(god, mes, i)}')
# # #         day = datetime.date(god, mes, i)
# # #         a = pytils.dt.ru_strftime(u"сегодня - %d %B %Y, %A", inflected=True, date=day)
# # #         print(a)
# #
# #
# # from django.shortcuts import render
# # import datetime
# # import calendar
# # import pytils
# # from pprint import pprint
# # # from models import Month
# #
# # # person = Month.objects.all()
# # c = calendar.Calendar()
# # today = datetime.datetime.now()
# # god, mes = today.year, today.month
# # now = pytils.dt.ru_strftime(u"%d - %a", inflected=True, date=today)
# # table = []
# # id = []
# # chislo = []
# # den_ned = []
# # pers_id = 1
# # supe_id = 1
# # da_of_we = []
# # for i in c.itermonthdays(god, mes):
# #     stro = []
# #     if i != 0:
# #         day = datetime.date(god, mes, i)
# #         dayy = str(day)
# #         # dayy = pytils.dt.ru_strftime(u"%D", inflected=True, date=day)
# #         n_d = calendar.weekday(god, mes, i)
# #         stroka = pytils.dt.ru_strftime(u"%Y-%B-%D", inflected=True, date=day)
# #         day_of_week  = pytils.dt.ru_strftime(u"%a", inflected=True, date=day)
# #         if n_d in range(5):
# #             stro.append(i)
# #             stro.append(dayy)
# #             stro.append(1)
# #             stro.append(1)
# #             stro.append(2)
# #             stro.append(day_of_week)
# #             table.append(stro)
# #
# #         elif n_d == 5:
# #             pass
# # content = {
# #     'title': 'Расписание дежурств',
# #     'txt': 'Расписание дежурств',
# #     'now': now,
# #     'table': table,
# #     # 'person': person,
# # }
# #
# # pprint(content)
# #
# #
# # # from duty.models import Month
# #
# #
# # import .models
#
#
# # import sqlite3
# # import datetime
# # from random import randint
# # print('читаем базу данных')
# # conn = sqlite3.connect(r'../../db.sqlite3')
# # cur = conn.cursor()
# # cur.execute("SELECT * FROM duty_static;")
# # all_results = cur.fetchall()
# # print(f'Выводим все значения - {all_results}')
# # for a_r in all_results:
# #     print(f'a_r = {a_r}')
# #
# # id = int(datetime.datetime.now().timestamp()) - 1611679693
# # log = randint(1, 1234)
# # logs = [id, log]
# # print(id)
# # print(f'добавляем в базу данных')
# # cur.execute("INSERT INTO duty_static VALUES(?,?);", logs)
# # conn.commit()
# #
# #
# #
# # conn.close()
# #
# # import hashlib
# #
# # a = [
# #     ['Белкин', 'C3888', '172.41.0.129'],
# #     ['Середа', 'С3535', '172.41.0.130'],
# #     ['Бунакова', 'С3537', '172.41.0.131'],
# #     ['Чуркина', 'C3251', '172.41.0.133'],
# #     ['Бирюкова', 'C3887', '172.41.0.134'],
# #     ['Изыльметьева', 'C3889', '172.41.0.137'],
# #     ['Серкова', 'C3886', '172.41.0.138'],
# #     ['Антипин', 'С3540', '172.41.0.139'],
# #     ['Семякина', 'C2652', '172.41.0.140'],
# #     ['--Соколов', 'C2972', '172.41.0.141'],
# #     ['Коршунова', 'С3221', '172.41.0.142'],
# #     ['Выборнова', 'C2860', '172.41.0.144'],
# #     ['Дубровина', 'C2654', '172.41.0.145'],
# #     ['Борщева', 'C3891', '172.41.0.147'],
# #     ['Сахно', 'C2655', '172.41.0.149'],
# #     ['Сосина', 'C3893', '172.41.0.152'],
# #     ['--Рябин', 'C2859', '172.41.0.153'],
# #     ['Смирнов', 'С3246', '172.41.0.154'],
# #     ['Поликарпов', 'C3230', '172.41.0.159'],
# #     ['Пономарева', 'C2973', '172.41.0.161'],
# #     ['Пирогов', 'C3884', '172.41.0.163'],
# #     ['Баранчугова', 'C3890', '172.41.0.164'],
# #     ['Сканер', 'C3236', '172.41.0.165'],
# #     ['Соколов', 'С3539', '172.41.0.166'],
# #     ['Рябин', 'C3892', '172.41.0.167'],
# #     ['Лаптенок', 'C3885', '172.41.0.168'],
# #     ['Апполонова', 'С3541', '172.41.0.169'],
# #     ['Смекалина', 'С3534', '172.41.0.170'],
# #     ['Вешонкина', 'С3536', '172.41.0.171'],
# #     ['Кузнецова', 'С4509', '172.41.0.172'],
# #     ['Скрипкин', 'С4512', '172.41.0.173'],
# #     ['Тихоненок', 'С4515', '172.41.0.174'],
# #     ['Гелеверя', 'С4517', '172.41.0.175'],
# #     ['Тарынина', 'С4511', '172.41.0.176'],
# #     ['Салимов', 'С4510', '172.41.0.177'],
# #     ['Алексеева', 'С4513', '172.41.0.178'],
# #     ['Каширский', 'С4506', '172.41.0.179'],
# #     ['Задонская', 'C2653', '172.41.0.181'],
# #     ['Муллагалеева', 'С4514', '172.41.0.183'],
# #     ['Кожевников', 'С4507', '172.41.0.184'],
# #     ['Темиргалеев', 'С4516', '172.41.0.188'],
# #     ['Шемякин', 'С4508', '172.41.0.192'],
# #     ['MacBook VPN', 'home', '10.0.0.5'],
# #     ['Kodachi VPN', 'home', '10.0.0.3'],
# #     ['localhost', 'localhost', '127.0.0.1'],
# #     ['MacBook', 'home', '192.168.88.253'],
# #     ['Kodachi', 'home', '192.168.88.227'],
# # ]
# # ip = b'172.41.0.174'
# #
# # for i, ob in enumerate(a):
# #     # print(f'{i}-{ob}')
# #     hash_object = hashlib.sha1(ob[2].encode())
# #     a[i].append(hash_object.hexdigest())
# #
# # for aa in a:
# #     print(f'{aa},')
#
# #################################################################################
# ################################# ПРОВЕРКА IP ###################################
# #################################################################################
# # # -*- coding: utf-8 -*-                                                       #
# # from ips import a                                                             #
# # import subprocess                                                             #
# # import platform                                                               #
# # def check(hosts):                                                             #
# #     name = hosts[0]                                                           #
# #     host = hosts[1].upper()                                                   #
# #     base_ip = hosts[2]                                                        #
# #     # print(f'Проверяем {host}')                                              #
# #     if host[:4] != '041-' and host != 'home' and host != 'localhost':         #
# #         host = '041-' + host                                                  #
# #         # print(f'Теперь все ОК - {host}')                                    #
# #     # else:                                                                   #
# #     #     print(f'{host} уже и так OK')                                       #
# #     ping_str = "-n 1" if platform.system().lower() == "windows" else "-c 1"   #
# #     args = "ping " + " " + ping_str + " " + host                              #
# #     # print(args)                                                             #
# #     try:                                                                      #
# #         con_out = subprocess.check_output(args, shell=True).decode('cp866')   #
# #         i = con_out.index('[') + 1                                            #
# #         p = con_out.index(']')                                                #
# #         ip = con_out[i:p]                                                     #
# #         i = con_out.index('[') + 1                                            #
# #         p = con_out.index(']')                                                #
# #         print(f'{name} - {host} - {ip}', end=' - ')                           3
# #         if base_ip == ip:                                                     3
# #             print(f'Все четко')                                               #
# #         else:                                                                 #
# #             print(f'ПАНИКА! ПОДМЕНА IP!!! \n {base_ip} != {ip}')              #
# #     except:                                                                   #
# #         # print(f'Фигня вышла - пропинговать не вышло')                       #
# #         print(f'{name} - {host} - {base_ip} - offline')                       #
# # for i, person in enumerate(a):                                                #
# #     check(person)                                                             #
# #################################################################################
# #################################################################################
#
#
# # from django.utils.safestring import mark_safe
# # from django import template
# # register = template.Library
# #
# # @register.filter (is_dafe=True)
# # def format_description(description):
# #     text = ''
# #     for i in description.split('\n'):
# #         text += ('<p>' + i + '</p>')
# #         return mark_safe(text)
# # print('12')
# # first_day = '2021-10-01'
# # first_month = int(first_day.split('-')[1])
# # print(f'{first_day = }')
# # print(f'{first_month = }')
# date_from_form = {''
#                   'person': ['29', '34', '22', '19', '28', '4', '19', '38',
#                              '13', '24', '11', '1', '12', '32', '20', '29'],
#                   'id': ['10', '11', '12', '13', '14', '17', '18', '19',
#                          '20', '21', '24', '25', '26', '27', '28', '31'],
#                   }
# persons = date_from_form["person"]
# print(f'{ persons =}')
# print(f'{date_from_form["id"] =}')
# print(f'{*persons, }')
#
# import datetime
#
#
# today = datetime.datetime.now()
# today.date()
# print(f'{today = }')
# print(f'{today.month = }')
# print(f'----------------------\n')
#
# print(f'{today.date() = }')
# peoples = [
#     ['Белкин', 'C3888', '172.41.0.129', '0c60055f2b435aca204a82987580290ff7bff461'],
#     ['Середа', 'C3535', '172.41.0.130', 'eb2cc1603e8d22f1f3d6de51f7ca84799fe75623'],
#     ['Бунакова', 'C3537', '172.41.0.131', '1f81c91f6c272b317fa3db9630f3603a221af664'],
#     ['Чуркина', 'C3251', '172.41.0.133', 'c375bd242b60423ef8e5902fbc3eb7864610d1c2'],
#     ['Гусев', 'C3887', '172.41.0.134', '2d5c6ca982ccb2038e68389cdf563130162e82d3'],
#     ['Семякина', 'C3889', '172.41.0.137', 'fbd090252878d2a8ec29a0e22d0e807874f6cafc'],
#     ['Серкова', 'C3886', '172.41.0.138', 'f06b8537ddbce7d01453423d239f4e909261b2cd'],
#     ['Антипин', 'C3540', '172.41.0.139', '16222ebeb801394cb869ec860cb48e3c80b1ce06'],
#     ['--Семякина', 'C2652', '172.41.0.140', '4cd574116138ffc20467884ca440968c3599835e'],
#     ['--Соколов', 'C2972', '172.41.0.141', '58de5afa48ce82ba1afd2bb63e8fc0123a9fb175'],
#     ['??Выборнова', 'C3221', '172.41.0.142', 'dd9578434e440de8abf0d6fad9404cd041c0a624'],
#     ['--Выборнова', 'C2860', '172.41.0.144', 'eaf2037d5253f0fa204aa1e73356c38bb1a45a8b'],
#     ['--Дубровина', 'C2654', '172.41.0.145', 'e8cce07cf8a369784ac600264fac0d36bc115404'],
#     ['Борщева', 'C3891', '172.41.0.147', 'ffa0892e921deaf50921ec608f8af8f7e949ea48'],
#     ['--Сахно', 'C2655', '172.41.0.149', '003d89eab2525dc7ae311848c51815f47aae0e28'],
#     ['Сосина', 'C3893', '172.41.0.152', 'b4e4d51fc3efcdeacc8ab3507419885bc2c87097'],
#     ['--Рябин', 'C2859', '172.41.0.153', '686e5ddf657ad05cc77de9265f35d6195ed6874a'],
#     ['Кочеряев', 'C3246', '172.41.0.154', '1006786b03dc970475ea60984eb8d59f957d5c04'],
#     ['--Поликарпов', 'C3230', '172.41.0.159', '79c411e3d71ac036987015c8bf549cc65e1c9e93'],
#     ['--Пономарева', 'C2973', '172.41.0.161', 'f464d6f0d3c5949d648e1dab3d46b97497f57fdf'],
#     ['Апполонова', 'C3884', '172.41.0.163', '17e0564293cc0dfc778b5828ab9948dcfa1f021a'],
#     ['Баранчугова', 'C3890', '172.41.0.164', '0dc2ee16a2118c9105eb3ae73abcc7765bb4de7b'],
#     ['--Сканер', 'C3236', '172.41.0.165', 'fd35e934d94661acef652a8d9544e7db4d94febc'],
#     ['Соколов', 'C3539', '172.41.0.166', 'cdafef5054246f7e5fd02ede9bf04b5951efadbc'],
#     ['Рябин', 'C3892', '172.41.0.167', '6304f214eaded0d08587605fc31b30aee9393aa2'],
#     ['Лаптенок', 'C3885', '172.41.0.168', 'eba535dcde4b3049c13041361ed77c8dcbe93dc3'],
#     ['C3541', 'C3541', '172.41.0.169', '349d28dc2118d5a6689324c754c03ed8b9952568'],
#     ['Смекалина', 'C3534', '172.41.0.170', '9cd871a1d21123a86f9d4ea673a0bf904e49c93d'],
#     ['Выборнова', 'C3536', '172.41.0.171', '6cbacff29b8c57562056e6254be29ac697f577bb'],
#     ['Кузнецова', 'C4509', '172.41.0.172', '87ee65f7072877a68ce5a4dc987e88e5004720cb'],
#     ['Скрипкин', 'C4512', '172.41.0.173', '42156231f7e40be652043419dd81e41eb35a6e3a'],
#     ['Тихоненок', 'C4515', '172.41.0.174', '0584d35887d1eb985941b1bf97571ba51d245e0e'],
#     ['Поликарпов', 'C4517', '172.41.0.175', '9cff70cdc998940a4be059ef12766272311768f6'],
#     ['Тарынина', 'C4511', '172.41.0.176', 'a8594d106e2520294796de56458185d777e6e56f'],
#     ['Салимов', 'C4510', '172.41.0.177', 'cbfde08b5e3da211fb90d6a7e8ef40a48ee4a2e0'],
#     ['Алексеева', 'C4513', '172.41.0.178', 'e6d0f4bd11fb1f0047e8a582e38dac16f0836ea9'],
#     ['Каширский', 'C4506', '172.41.0.179', 'b654bb5521482dfc5bca4266636992aab4a1fb91'],
#     ['Задонская', 'C2653', '172.41.0.181', '9f0faabedce891e8f1d34a8ce7416c7755beb125'],
#     ['Муллагалеева', 'C4514', '172.41.0.183', 'cda52c9bb256a606cdc4cb33e4c686400ae74119'],
#     ['Кожевников', 'C4507', '172.41.0.184', 'c7d80ab030202cb59775efdc768fecaced54fcb3'],
#     ['Темиргалеев', 'C4516', '172.41.0.188', '74620af4882e8e7244daf1060d99d29fda2cb1fe'],
#     ['Шемякин', 'C4508', '172.41.0.192', '4a5c29a93c085b7eea81c3a2d6d911e5ca791f1b'],
#     ['MacBook VPN', 'home', '10.0.0.5', '00d735369988d4bbd0d404a166a6f8b871027763'],
#     ['Kodachi VPN', 'home', '10.0.0.3', 'd854e2039a3e27436167f5e1bd2b0544a1fddd7d'],
#     ['localhost', 'localhost', '127.0.0.1', '4b84b15bff6ee5796152495a230e45e3d7e947d9'],
#     ['MacBook', 'home', '192.168.88.253', 'a7f5f7e93e89ff3d2b8e5d0dec876268e74c038c'],
#     ['Kodachi', 'home', '192.168.88.227', '6875936c22ff4e8ccb6da5ddba4ba22667bdb08c'],
#     ['Хомяков', 'C3538', '172.41.0.132',  '1680050e21c86c6a256aa275232ff13a2f6bfe0e'],
#     #['Гусев', 'C3538', '172.41.0.132',  '1680050e21c86c6a256aa275232ff13a2f6bfe0e'],
#
# ]
# peoples = [
#     ['-C2860', 'C2860', '172.41.0.144', 'eaf2037d5253f0fa204aa1e73356c38bb1a45a8b'],
#     ['-C2654', 'C2654', '172.41.0.145', 'e8cce07cf8a369784ac600264fac0d36bc115404'],
#     ['-C3230', 'C3230', '172.41.0.159', '79c411e3d71ac036987015c8bf549cc65e1c9e93'],
#     ['-C2973', 'C2973', '172.41.0.161', 'f464d6f0d3c5949d648e1dab3d46b97497f57fdf'],
#     ['-C2859', 'C2859', '172.41.0.153', '686e5ddf657ad05cc77de9265f35d6195ed6874a'],
#     ['-C2655', 'C2655', '172.41.0.149', '003d89eab2525dc7ae311848c51815f47aae0e28'],
#     ['-C2652', 'C2652', '172.41.0.140', '4cd574116138ffc20467884ca440968c3599835e'],
#     ['-C3236', 'C3236', '172.41.0.165', 'fd35e934d94661acef652a8d9544e7db4d94febc'],
#     ['-C2972', 'C2972', '172.41.0.141', '58de5afa48ce82ba1afd2bb63e8fc0123a9fb175'],
#     ['Монтажники С3221', 'C3221', '172.41.0.142', 'dd9578434e440de8abf0d6fad9404cd041c0a624'],
#     ['Текстовики C3541', 'C3541', '172.41.0.169', '349d28dc2118d5a6689324c754c03ed8b9952568'],
#     ['Kodachi', 'home', '192.168.88.227', '6875936c22ff4e8ccb6da5ddba4ba22667bdb08c'],
#     ['Kodachi VPN', 'home', '10.0.0.3', 'd854e2039a3e27436167f5e1bd2b0544a1fddd7d'],
#     ['MacBook', 'home', '192.168.88.253', 'a7f5f7e93e89ff3d2b8e5d0dec876268e74c038c'],
#     ['MacBook VPN', 'home', '10.0.0.5', '00d735369988d4bbd0d404a166a6f8b871027763'],
#     ['localhost', 'localhost', '127.0.0.1', '4b84b15bff6ee5796152495a230e45e3d7e947d9'],
#     ['Алексеева', 'C4513', '172.41.0.178', 'e6d0f4bd11fb1f0047e8a582e38dac16f0836ea9'],
#     ['Антипин', 'C3540', '172.41.0.139', '16222ebeb801394cb869ec860cb48e3c80b1ce06'],
#     ['Апполонова', 'C3884', '172.41.0.163', '17e0564293cc0dfc778b5828ab9948dcfa1f021a'],
#     ['Баранчугова', 'C3890', '172.41.0.164', '0dc2ee16a2118c9105eb3ae73abcc7765bb4de7b'],
#     ['Белкин', 'C3888', '172.41.0.129', '0c60055f2b435aca204a82987580290ff7bff461'],
#     ['Борщева', 'C3891', '172.41.0.147', 'ffa0892e921deaf50921ec608f8af8f7e949ea48'],
#     ['Бунакова', 'C3537', '172.41.0.131', '1f81c91f6c272b317fa3db9630f3603a221af664'],
#     ['Выборнова', 'C3536', '172.41.0.171', '6cbacff29b8c57562056e6254be29ac697f577bb'],
#     ['Гусев', 'C3887', '172.41.0.134', '2d5c6ca982ccb2038e68389cdf563130162e82d3'],
#     ['-C2653', 'C2653', '172.41.0.181', '9f0faabedce891e8f1d34a8ce7416c7755beb125'],
#     ['Каширский', 'C4506', '172.41.0.179', 'b654bb5521482dfc5bca4266636992aab4a1fb91'],
#     ['Кожевников', 'C4507', '172.41.0.184', 'c7d80ab030202cb59775efdc768fecaced54fcb3'],
#     ['Кочеряев', 'C3246', '172.41.0.154', '1006786b03dc970475ea60984eb8d59f957d5c04'],
#     ['Кузнецова', 'C4509', '172.41.0.172', '87ee65f7072877a68ce5a4dc987e88e5004720cb'],
#     ['Лаптенок', 'C3885', '172.41.0.168', 'eba535dcde4b3049c13041361ed77c8dcbe93dc3'],
#     ['Муллагалеева', 'C4514', '172.41.0.183', 'cda52c9bb256a606cdc4cb33e4c686400ae74119'],
#     ['Поликарпов', 'C4517', '172.41.0.175', '9cff70cdc998940a4be059ef12766272311768f6'],
#     ['Рябин', 'C3892', '172.41.0.167', '6304f214eaded0d08587605fc31b30aee9393aa2'],
#     ['Салимов', 'C4510', '172.41.0.177', 'cbfde08b5e3da211fb90d6a7e8ef40a48ee4a2e0'],
#     ['Семякина', 'C3889', '172.41.0.137', 'fbd090252878d2a8ec29a0e22d0e807874f6cafc'],
#     ['-Середа', 'C3535', '172.41.0.130', 'eb2cc1603e8d22f1f3d6de51f7ca84799fe75623'],
#     ['Серкова', 'C3886', '172.41.0.138', 'f06b8537ddbce7d01453423d239f4e909261b2cd'],
#     ['Скрипкин', 'C4512', '172.41.0.173', '42156231f7e40be652043419dd81e41eb35a6e3a'],
#     ['Смекалина', '-C3534', '172.41.0.170', '9cd871a1d21123a86f9d4ea673a0bf904e49c93d'],
#     ['Соколов', 'C3539', '172.41.0.166', 'cdafef5054246f7e5fd02ede9bf04b5951efadbc'],
#     ['Сосина', 'C3893', '172.41.0.152', 'b4e4d51fc3efcdeacc8ab3507419885bc2c87097'],
#     ['Тарынина', 'C4511', '172.41.0.176', 'a8594d106e2520294796de56458185d777e6e56f'],
#     ['Темиргалеев', 'C4516', '172.41.0.188', '74620af4882e8e7244daf1060d99d29fda2cb1fe'],
#     ['Тихоненок', 'C4515', '172.41.0.174', '0584d35887d1eb985941b1bf97571ba51d245e0e'],
#     ['Хомяков', 'C3538', '172.41.0.132', '1680050e21c86c6a256aa275232ff13a2f6bfe0e'],
#     ['Чуркина', 'C3251', '172.41.0.133', 'c375bd242b60423ef8e5902fbc3eb7864610d1c2'],
#     ['Шемякин', 'C4508', '172.41.0.192', '4a5c29a93c085b7eea81c3a2d6d911e5ca791f1b'],
# ]
# print(f'peoples = [')
# for i in sorted(peoples):
#     print(f'    {i},')
# print(f']')
