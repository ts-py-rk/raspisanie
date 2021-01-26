from django.shortcuts import render
from django.contrib import admin
import datetime
import pytils
from .models import Month
from .models import People
from .ips import a

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

    content = {
        'title': 'Расписание дежурств',
        'txt': 'Дежурства',
        'now': now,
        'wtf': stroki,
    }
    def client_ip(reguest):
        x_forwardwd_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwardwd_for:
            ip = x_forwardwd_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        for i in a:
            if i[2] == ip:
                posetil = f'{i[1]} - {i[0]} - {i[2]}'
        print(f'Сайт открыл  {datetime.datetime.now()} - {posetil}')
        print(type(ip))
        with open('ip.txt', 'a', encoding='utf-8') as bas:
            bas.write(f"{datetime.datetime.now()} - {posetil} \n")
        return
    client_ip(request)
    return render(request, 'duty/index.html', content)


def stat(request):

    content = {
        'spisok' : [
    '2021 - 01 - 26 13:27: 46.560003 - С4515 - Тихоненок - 172.41.0.174',
    '2021 - 01 - 26  13: 28:53.120967 - С4513 - Алексеева - 172.41.0.178',
    '2021 - 01 - 26  14: 10:23.572228 - C3893 - Сосина - 172.41.0.152',
    ]
    }

    return render(request, 'duty/stat.html', content)