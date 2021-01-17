from django.shortcuts import render
from django.urls import path
from django.contrib import admin
import datetime
import calendar
import pytils
from .models import Month
from .models import People

def index(request):
    # m = Month.objects.get('name')
    c = calendar.Calendar()
    p = People.id
    today = datetime.datetime.now()
    god, mes = today.year, today.month
    now = pytils.dt.ru_strftime(u"%d - %a", inflected=True, date=today)
    # now = pytils.dt.ru_strftime(u"сегодня - %d %B %Y, %A", inflected=True, date=today)
    table = []
    # id = []
    chislo = []
    den_ned = []
    pers_id = 1
    supe_id = 1
    da_of_we = []
    stroki = []
    www = []
    wtf = Month.objects.in_bulk()
    for w in wtf:
        strochka = []
        strochka.append(wtf[w].day_of_week)
        strochka.append(wtf[w].id)
        stroki.append(strochka)

    for i in c.itermonthdays(god, mes):
        stro = []
        if i != 0:
            day = datetime.date(god, mes, i)
            dayy = str(day)
            n_d = calendar.weekday(god, mes, i)
            stroka = pytils.dt.ru_strftime(u"%Y-%B-%D", inflected=True, date=day)

            day_of_week = pytils.dt.ru_strftime(u"%a", inflected=True, date=day)
            if n_d in range(5):
                # stro.append(dayy)
                # stro.append(1)
                # stro.append(1)
                # stro.append(2)
                stro.append(day_of_week)
                stro.append(i)
                # stro.append(wtf)
                table.append(stro)

            elif n_d == 5:
                pass
    content = {
        'title': 'Расписание дежурств',
        'txt': 'Расписание дежурств',
        'now': now,
        'table': table,
        # 'months': months,
        # 'test' : Month.objects.get(id='day')
        'people': p,
        'wtf': stroki,
    }
    return render(request, 'duty/index.html', content)


