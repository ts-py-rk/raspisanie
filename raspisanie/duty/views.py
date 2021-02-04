from django.shortcuts import render
from django.contrib import admin
import datetime
import pytils
from .models import Month
from .models import People
from .ips import a
import sqlite3


def index(request):
    today = datetime.datetime.now()
    now = int(pytils.dt.ru_strftime(u"%d", inflected=True, date=today))
    stroki = []

    wtf = Month.objects.in_bulk()
    for w in wtf:
        strochka = []
        d_n = wtf[w].day_of_week
        ch = wtf[w].id
        id_d = wtf[w].person_id
        strochka.append(d_n)
        strochka.append(ch)
        imena = People.objects.in_bulk()
        for im in imena:
            if imena[im].id == id_d:
                strochka.append(imena[im].familia)
        stroki.append(strochka)

    def client_ip(reguest):
        x_forwardwd_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwardwd_for:
            ip = x_forwardwd_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        vremya = datetime.datetime.now().replace(microsecond=0)
        print(f'ip = {vremya} - {ip}')
        if ip != '172.41.0.174' and ip != '172.41.0.178' and ip != '192.168.88.253':
        # if ip != '172.41.0.174' and ip != '172.41.0.178':
        # if ip != '172.41.0.174':
        # if ip != '172.41.0.178':
            for i in a:
                if i[2] == ip:
                    posetitel = f'{i[1]} - {i[0]}'
                    posesenie = f'{vremya} - {posetitel}'
                    # print(f'posetitel = {posetitel}')
                    # print(f'vremya = {vremya}')
                    print(f'posesenie = {posesenie}')
                    break
                else:
                    posesenie = f'{vremya} - Кто то неизвестный - {ip}'
            # читаем базу данных
            conn = sqlite3.connect(r'db.sqlite3')
            cur = conn.cursor()
            cur.execute("SELECT * FROM duty_static;")
            id = int(datetime.datetime.now().timestamp()) - 1611679693
            logs = [id, posesenie]
            # добавляем в базу данных
            cur.execute("INSERT INTO duty_static VALUES(?,?);", logs)
            conn.commit()
            conn.close()
        return

    client_ip(request)
    content = {
        'title': 'Расписание дежурств',
        'txt': 'Дежурства',
        'now': now,
        'wtf': stroki,
    }
    return render(request, 'duty/index.html', content)


def stat(request):
    x_forwardwd_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwardwd_for:
        ip = x_forwardwd_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    if ip == '172.41.0.174' or ip == '172.41.0.178' or ip == '192.168.88.253':
    # if ip == '172.41.0.174' or ip == '172.41.0.178':
        conn = sqlite3.connect(r'db.sqlite3')
        cur = conn.cursor()
        cur.execute("SELECT * FROM duty_static;")
        all_results = cur.fetchall()
        conn.close()
        title = 'Статистика посещений'
    else:
        all_results = [['','Error 404'],[]]
        title = 'Страница не найдена'
    content = {
        'zagolovok': title,
        'spisok' : all_results,
    }

    return render(request, 'duty/stat.html', content)


def news(request):
    title = 'Новости'
    content = {
        'title': title,
    }
    return render(request, 'duty/news.html', content)

def otvet(request):
    title = 'Ответственные дежурные'
    content = {
        'title': title,
    }
    return render(request, 'duty/otvet.html', content)

def rules(request):
    title = 'Положение о дежурстве'
    content = {
        'title': title,
    }
    return render(request, 'duty/rules.html', content)

def help(request):
    title = 'Справка'
    content = {
        'title': title,
    }
    return render(request, 'duty/help.html', content)

