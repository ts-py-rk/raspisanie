from django.shortcuts import render
import datetime
import calendar
import pytils

def index(request):

    c = calendar.Calendar()
    today = datetime.datetime.now()
    god, mes = today.year, today.month
    now = pytils.dt.ru_strftime(u"%d - %a", inflected=True, date=today)
    # now = pytils.dt.ru_strftime(u"сегодня - %d %B %Y, %A", inflected=True, date=today)
    table = []

    # print(now, '\n')

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
            else:                       #
                table.append(stroka)    # надо будет убрать


    content = {
        'title': 'Расписание дежурств',
        'txt': 'Расписание дежурств',
        'now': now,
        'table': table,
    }
    return render(request, 'duty/index.html', content)