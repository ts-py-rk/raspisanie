from django.shortcuts import render
from django.urls import path
from django.contrib import admin
import datetime
import calendar
import pytils
from .models import Month
from .models import People

def index(request):
    c = calendar.Calendar()
    p = People.id
    today = datetime.datetime.now()
    god, mes = today.year, today.month
    now = pytils.dt.ru_strftime(u"%d - %a", inflected=True, date=today)
    table = []
    stroki = []

    wtf = Month.objects.in_bulk()
    for w in wtf:
        strochka = []
        d_n = wtf[w].day_of_week
        ch = wtf[w].id
        id_d = wtf[w].person_id
        strochka.append(d_n)
        strochka.append(ch)
        # strochka.append(id_d)

        imena = People.objects.in_bulk()
        for im in imena:
            if imena[im].id == id_d:
                strochka.append(imena[im].familia)

        stroki.append(strochka)

    #######################################
    # # # # # # ЭТО РАБОТАЕТ!!! # # # # # #
    #######################################
    # wtf = People.objects.in_bulk()
    # for w in wtf:
    #     strochka = []
    #     strochka.append(wtf[w].id)
    #     strochka.append(wtf[w].imya)
    #     strochka.append(wtf[w].familia)
    #     stroki.append(strochka)
    #######################################


    for i in c.itermonthdays(god, mes):
        stro = []
        if i != 0:
            day = datetime.date(god, mes, i)
            n_d = calendar.weekday(god, mes, i)

            day_of_week = pytils.dt.ru_strftime(u"%a", inflected=True, date=day)
            if n_d in range(5):
                stro.append(day_of_week)
                stro.append(i)
                table.append(stro)

            elif n_d == 5:
                pass
    content = {
        'title': 'Расписание дежурств',
        'txt': 'Дежурства',
        'now': now,
        'wtf': stroki,
    }
    return render(request, 'duty/index.html', content)


