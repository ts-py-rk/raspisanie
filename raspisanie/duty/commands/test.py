import datetime
import calendar
# from django.template.defaultfilters import date
# from django.utils.translation import get_language, activate
#
# today = datetime.datetime.now()
# # month = today.month
# # print (month)
# # print(today.strftime('%B'))
# # today = datetime.date.today()
# # # print(date(today, 'F'))
# # # month = calendar.month_name[1]
# # # print(month)
# #
# # # import mptt
# # # print(mptt.VERSION)
# # # # (0, 5, '+dev')
import pytils
# # b = pytils.numeral.get_plural(1, u"гвоздь, гвоздя, гвоздей")
# # print(b)
# # # c = pytils.dt.ru_strftime(u"сегодня - %d %B %Y, %A", inflected=True, date=datetime.date(2006, 9, 2))
# # c = pytils.dt.ru_strftime(u"сегодня - %d %B %Y, %A", inflected=True, date=today)
# day_of_week = pytils.dt.ru_strftime(u"%A", inflected=True, date=today)
# print(c)
# # # dow = datetime.datetime.weekday()
# # d_o_w = datetime.datetime.isoweekday(today)
# # # d_o_w = datetime.datetime.isoweekday(dow)
# # print(d_o_w)
#
#
# # mesyas = range(1,13)
# # for m in mesyas:
# #     # print(m)
# #     today = datetime.date(2020, m, 1)
# #     # print(f'{today.year} год, {today.month} месяц, {today.day} число')
# #     print(f'{pytils.dt.ru_strftime(u"сегодня  %a - %d %B %Y", inflected=True, date=today)}')
# #     # for d in today.day:
# #     #     print(d)
# # #
# # # print(today.year)
# # # mesyas = today.month
# # # # m = pytils.dt.ru_strftime(u'%B', date=mesyas)
# # # print(mesyas)
#
# # def date_iter(year, month):
# #     # cal = calendar.Calendar
# #     for i in range(1, calendar.monthrange(year, month)[0] + 1):
# #         yield date(year, month, i)
# #     # cal.itermonthdays(year, month)
# # #     # return cal.itermonthdates(calendar, month, year)
# # #
# # #
# # for d in date_iter(2019, 12):
# #     print(d)
# #
# # # print(date_iter(2019, 12))
#
# kalendar = calendar.Calendar(firstweekday=0)
# year = 2021
# month = 1
# test = calendar.monthrange(year, month)  # день недели первого дня месяца и количество дней в этом месяце
# print(test)
# # yanvar = calendar.itermonthday(year,month)
#
# # for i in yanvar:
# #     print(i)
#
# # for month in range (1, 13):
# #     macal = calendar.monthcalendar(2021, month)
# #     week1 = macal[0]
# #     week2 = macal[1]
# #
# #     if week1[calendar.MONDAY] != 0:
# #         auditday = week1[calendar.MONDAY]
# #     else:
# #         auditday = week2[calendar.MONDAY]
# #     print("%10s %2d" % (calendar.month_name[month], auditday))
#
# # import calendar
# # Создаем обычный текстовый календарь
# c = calendar.TextCalendar(calendar.THURSDAY)
# str = c.formatmonth(2025, 1, 0, 0)
# print (str)
# # перебираем через цикл дни месяца
# # нули указывают, что дни принадлежат смежному месяцу
# god = 2021
# mes = 1
# day_of_week = pytils.dt.ru_strftime(u"%A", inflected=True, date=today)
# for i in c.itermonthdays(god, mes):
#     if i != 0:
#         # print (f'{i} - {calendar.weekday(god, mes, i)}')
#         day = datetime.date(god, mes, i)
#         a = pytils.dt.ru_strftime(u"сегодня - %d %B %Y, %A", inflected=True, date=day)
#         print(a)




import datetime
import calendar

c = calendar.Calendar()
today = datetime.datetime.now()
god, mes = today.year, today.month
now = pytils.dt.ru_strftime(u"сегодня - %d %B %Y, %A", inflected=True, date=today)
table = []

print(now, '\n')

for i in c.itermonthdays(god, mes):
    if i != 0:
        day = datetime.date(god, mes, i)
        n_d = calendar.weekday(god, mes, i)
        stroka = pytils.dt.ru_strftime(u"%d - %a", inflected=True, date=day)
        if n_d in range(5):
            # print(f'{stroka}')
            table.append(stroka)
        elif n_d == 5:
            # print(' ')
            table.append('')

for t in table:
    print(t)

{% if {{now}} %}
{% else %}
{% endif}