# import datetime
# import calendar
# # from django.template.defaultfilters import date
# # from django.utils.translation import get_language, activate
# #
# # today = datetime.datetime.now()
# # # month = today.month
# # # print (month)
# # # print(today.strftime('%B'))
# # # today = datetime.date.today()
# # # # print(date(today, 'F'))
# # # # month = calendar.month_name[1]
# # # # print(month)
# import pytils
# # # b = pytils.numeral.get_plural(1, u"гвоздь, гвоздя, гвоздей")
# # # print(b)
# # # # c = pytils.dt.ru_strftime(u"сегодня - %d %B %Y, %A", inflected=True, date=datetime.date(2006, 9, 2))
# # # c = pytils.dt.ru_strftime(u"сегодня - %d %B %Y, %A", inflected=True, date=today)
# # day_of_week = pytils.dt.ru_strftime(u"%A", inflected=True, date=today)
# # print(c)
# # # # dow = datetime.datetime.weekday()
# # # d_o_w = datetime.datetime.isoweekday(today)
# # # # d_o_w = datetime.datetime.isoweekday(dow)
# # # print(d_o_w)
# #
# #
# # # mesyas = range(1,13)
# # # for m in mesyas:
# # #     # print(m)
# # #     today = datetime.date(2020, m, 1)
# # #     # print(f'{today.year} год, {today.month} месяц, {today.day} число')
# # #     print(f'{pytils.dt.ru_strftime(u"сегодня  %a - %d %B %Y", inflected=True, date=today)}')
# # #     # for d in today.day:
# # #     #     print(d)
# # # #
# # # # print(today.year)
# # # # mesyas = today.month
# # # # # m = pytils.dt.ru_strftime(u'%B', date=mesyas)
# # # # print(mesyas)
# #
# # # def date_iter(year, month):
# # #     # cal = calendar.Calendar
# # #     for i in range(1, calendar.monthrange(year, month)[0] + 1):
# # #         yield date(year, month, i)
# # #     # cal.itermonthdays(year, month)
# # # #     # return cal.itermonthdates(calendar, month, year)
# # # #
# # # #
# # # for d in date_iter(2019, 12):
# # #     print(d)
# # #
# # # # print(date_iter(2019, 12))
# #
# # kalendar = calendar.Calendar(firstweekday=0)
# # year = 2021
# # month = 1
# # test = calendar.monthrange(year, month)  # день недели первого дня месяца и количество дней в этом месяце
# # print(test)
# # # yanvar = calendar.itermonthday(year,month)
# #
# # # for i in yanvar:
# # #     print(i)
# #
# # # for month in range (1, 13):
# # #     macal = calendar.monthcalendar(2021, month)
# # #     week1 = macal[0]
# # #     week2 = macal[1]
# # #
# # #     if week1[calendar.MONDAY] != 0:
# # #         auditday = week1[calendar.MONDAY]
# # #     else:
# # #         auditday = week2[calendar.MONDAY]
# # #     print("%10s %2d" % (calendar.month_name[month], auditday))
# #
# # # import calendar
# # # Создаем обычный текстовый календарь
# # c = calendar.TextCalendar(calendar.THURSDAY)
# # str = c.formatmonth(2025, 1, 0, 0)
# # print (str)
# # # перебираем через цикл дни месяца
# # # нули указывают, что дни принадлежат смежному месяцу
# # god = 2021
# # mes = 1
# # day_of_week = pytils.dt.ru_strftime(u"%A", inflected=True, date=today)
# # for i in c.itermonthdays(god, mes):
# #     if i != 0:
# #         # print (f'{i} - {calendar.weekday(god, mes, i)}')
# #         day = datetime.date(god, mes, i)
# #         a = pytils.dt.ru_strftime(u"сегодня - %d %B %Y, %A", inflected=True, date=day)
# #         print(a)
#
#
# from django.shortcuts import render
# import datetime
# import calendar
# import pytils
# from pprint import pprint
# # from models import Month
#
# # person = Month.objects.all()
# c = calendar.Calendar()
# today = datetime.datetime.now()
# god, mes = today.year, today.month
# now = pytils.dt.ru_strftime(u"%d - %a", inflected=True, date=today)
# table = []
# id = []
# chislo = []
# den_ned = []
# pers_id = 1
# supe_id = 1
# da_of_we = []
# for i in c.itermonthdays(god, mes):
#     stro = []
#     if i != 0:
#         day = datetime.date(god, mes, i)
#         dayy = str(day)
#         # dayy = pytils.dt.ru_strftime(u"%D", inflected=True, date=day)
#         n_d = calendar.weekday(god, mes, i)
#         stroka = pytils.dt.ru_strftime(u"%Y-%B-%D", inflected=True, date=day)
#         day_of_week  = pytils.dt.ru_strftime(u"%a", inflected=True, date=day)
#         if n_d in range(5):
#             stro.append(i)
#             stro.append(dayy)
#             stro.append(1)
#             stro.append(1)
#             stro.append(2)
#             stro.append(day_of_week)
#             table.append(stro)
#
#         elif n_d == 5:
#             pass
# content = {
#     'title': 'Расписание дежурств',
#     'txt': 'Расписание дежурств',
#     'now': now,
#     'table': table,
#     # 'person': person,
# }
#
# pprint(content)
#
#
# # from duty.models import Month
#
#
# import .models


# import sqlite3
# import datetime
# from random import randint
# print('читаем базу данных')
# conn = sqlite3.connect(r'../../db.sqlite3')
# cur = conn.cursor()
# cur.execute("SELECT * FROM duty_static;")
# all_results = cur.fetchall()
# print(f'Выводим все значения - {all_results}')
# for a_r in all_results:
#     print(f'a_r = {a_r}')
#
# id = int(datetime.datetime.now().timestamp()) - 1611679693
# log = randint(1, 1234)
# logs = [id, log]
# print(id)
# print(f'добавляем в базу данных')
# cur.execute("INSERT INTO duty_static VALUES(?,?);", logs)
# conn.commit()
#
#
#
# conn.close()
#
# import hashlib
#
# a = [
#     ['Белкин', 'C3888', '172.41.0.129'],
#     ['Середа', 'С3535', '172.41.0.130'],
#     ['Бунакова', 'С3537', '172.41.0.131'],
#     ['Чуркина', 'C3251', '172.41.0.133'],
#     ['Бирюкова', 'C3887', '172.41.0.134'],
#     ['Изыльметьева', 'C3889', '172.41.0.137'],
#     ['Серкова', 'C3886', '172.41.0.138'],
#     ['Антипин', 'С3540', '172.41.0.139'],
#     ['Семякина', 'C2652', '172.41.0.140'],
#     ['--Соколов', 'C2972', '172.41.0.141'],
#     ['Коршунова', 'С3221', '172.41.0.142'],
#     ['Выборнова', 'C2860', '172.41.0.144'],
#     ['Дубровина', 'C2654', '172.41.0.145'],
#     ['Борщева', 'C3891', '172.41.0.147'],
#     ['Сахно', 'C2655', '172.41.0.149'],
#     ['Сосина', 'C3893', '172.41.0.152'],
#     ['--Рябин', 'C2859', '172.41.0.153'],
#     ['Смирнов', 'С3246', '172.41.0.154'],
#     ['Поликарпов', 'C3230', '172.41.0.159'],
#     ['Пономарева', 'C2973', '172.41.0.161'],
#     ['Пирогов', 'C3884', '172.41.0.163'],
#     ['Баранчугова', 'C3890', '172.41.0.164'],
#     ['Сканер', 'C3236', '172.41.0.165'],
#     ['Соколов', 'С3539', '172.41.0.166'],
#     ['Рябин', 'C3892', '172.41.0.167'],
#     ['Лаптенок', 'C3885', '172.41.0.168'],
#     ['Апполонова', 'С3541', '172.41.0.169'],
#     ['Смекалина', 'С3534', '172.41.0.170'],
#     ['Вешонкина', 'С3536', '172.41.0.171'],
#     ['Кузнецова', 'С4509', '172.41.0.172'],
#     ['Скрипкин', 'С4512', '172.41.0.173'],
#     ['Тихоненок', 'С4515', '172.41.0.174'],
#     ['Гелеверя', 'С4517', '172.41.0.175'],
#     ['Тарынина', 'С4511', '172.41.0.176'],
#     ['Салимов', 'С4510', '172.41.0.177'],
#     ['Алексеева', 'С4513', '172.41.0.178'],
#     ['Каширский', 'С4506', '172.41.0.179'],
#     ['Задонская', 'C2653', '172.41.0.181'],
#     ['Муллагалеева', 'С4514', '172.41.0.183'],
#     ['Кожевников', 'С4507', '172.41.0.184'],
#     ['Темиргалеев', 'С4516', '172.41.0.188'],
#     ['Шемякин', 'С4508', '172.41.0.192'],
#     ['MacBook VPN', 'home', '10.0.0.5'],
#     ['Kodachi VPN', 'home', '10.0.0.3'],
#     ['localhost', 'localhost', '127.0.0.1'],
#     ['MacBook', 'home', '192.168.88.253'],
#     ['Kodachi', 'home', '192.168.88.227'],
# ]
# ip = b'172.41.0.174'
#
# for i, ob in enumerate(a):
#     # print(f'{i}-{ob}')
#     hash_object = hashlib.sha1(ob[2].encode())
#     a[i].append(hash_object.hexdigest())
#
# for aa in a:
#     print(f'{aa},')

#################################################################################
################################# ПРОВЕРКА IP ###################################
#################################################################################
# # -*- coding: utf-8 -*-                                                       #
# from ips import a                                                             #
# import subprocess                                                             #
# import platform                                                               #
# def check(hosts):                                                             #
#     name = hosts[0]                                                           #
#     host = hosts[1].upper()                                                   #
#     base_ip = hosts[2]                                                        #
#     # print(f'Проверяем {host}')                                              #
#     if host[:4] != '041-' and host != 'home' and host != 'localhost':         #
#         host = '041-' + host                                                  #
#         # print(f'Теперь все ОК - {host}')                                    #
#     # else:                                                                   #
#     #     print(f'{host} уже и так OK')                                       #
#     ping_str = "-n 1" if platform.system().lower() == "windows" else "-c 1"   #
#     args = "ping " + " " + ping_str + " " + host                              #
#     # print(args)                                                             #
#     try:                                                                      #
#         con_out = subprocess.check_output(args, shell=True).decode('cp866')   #
#         i = con_out.index('[') + 1                                            #
#         p = con_out.index(']')                                                #
#         ip = con_out[i:p]                                                     #
#         i = con_out.index('[') + 1                                            #
#         p = con_out.index(']')                                                #
#         print(f'{name} - {host} - {ip}', end=' - ')                           3
#         if base_ip == ip:                                                     3
#             print(f'Все четко')                                               #
#         else:                                                                 #
#             print(f'ПАНИКА! ПОДМЕНА IP!!! \n {base_ip} != {ip}')              #
#     except:                                                                   #
#         # print(f'Фигня вышла - пропинговать не вышло')                       #
#         print(f'{name} - {host} - {base_ip} - offline')                       #
# for i, person in enumerate(a):                                                #
#     check(person)                                                             #
#################################################################################
#################################################################################
