from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import datetime
import pytils
from .models import Month
from .models import People
from .models import Article
from .models import Static
from .models import SuperDuty
from .commands import otdel
import sqlite3
import hashlib
from .commands import month2
import logging
logging.basicConfig(filename='./log.log', level=logging.DEBUG, format='%(levelname)s - %(message)s')
# logging.basicConfig(filename='./log.log', level=logging.DEBUG, format='%(levelname)s - %(message)s', filemode='a')


good_ips = [
    '172.41.0.174',     # Я
    '172.41.0.178',     # Ирина
    '192.168.88.253',   # macbook
    '192.168.88.227',   # kodachi
    '10.0.0.100',       # Ирина vpn
    '10.0.0.5',         # macbook vpn
    '10.0.0.3',         # kodachi vpn
    '10.0.0.2',         # iphone vpn
    '127.0.0.1',        # localhost
]
qr_list = [
    # '172.41.0.173',       # Скрипкин
    # '172.41.0.192',       # Шемякин
    # '172.41.0.174',     # Я
    # '172.41.0.178',     # Ирина
    # '172.41.0.168',     # Таня

]
bad_ip = [
    # '172.41.0.174',  # Я
    '',
]
ip_otv_de = [
    '172.41.0.192',     # Шемякин
]
peoples = otdel.peoples
mon_fro_bas = month2.month_from_base()
now_mon = month2.now_month()
month2.check(mon_fro_bas, now_mon)


def reff(ip, qr_list):
    if ip in qr_list:
        qr = 'on'
    else:
        qr = 'off'
    return qr

def now_next_month():
    # logging.info(f'start next_month():')
    today = datetime.datetime.now()
    # logging.debug(f'    {today = }')
    now_month = today.month
    # logging.debug(f'    {now_month = }')
    if now_month < 12:
        # logging.debug(f'    now_month < 12:')
        next_month = now_month + 1
        # logging.debug(f'        {next_month = }')
    else:
        # logging.debug(f'    now_month >= 12:')
        next_month = 1
        # logging.debug(f'        {next_month = }')
    date_next_month = datetime.date(today.year, next_month, 1)
    # logging.debug(f'    {date_next_month = }')
    now_month_ru = pytils.dt.ru_strftime(
        u"%B",
        inflected=False,
        date=today
    )
    now_month_ru = now_month_ru.capitalize()
    # logging.debug(f'    {now_month_ru = }')
    next_month_ru = pytils.dt.ru_strftime(
        u"%B",
        inflected=False,
        date=date_next_month
    )
    next_month_ru = next_month_ru.capitalize()
    # logging.debug(f'    {next_month_ru = }')
    # logging.info(f'stop next_month()')
    return now_month, now_month_ru, next_month, next_month_ru

def now_next_duter(now_month_n, next_month_n, list=None):
    # logging.info(f'start now_next_duter({now_month_n}, {next_month_n}, {list}')
    imena = People.objects.in_bulk()
    # logging.debug(f'{imena = }')
    duters = SuperDuty.objects.in_bulk()
    # logging.debug(f'{duters = }')
    duters_list = []
    # logging.debug(f'{duters_list = }')
    for id in duters:
        # logging.debug(f'    {id = }')
        duter_id = duters[id].person_id
        # logging.debug(f'    {duter_id = }')
        duter_familia = imena[duter_id].familia
        # logging.debug(f'    {duter_familia = }')
        duter_month = duters[id].mesyas
        # logging.debug(f'    {duter_month = }')
        duter_month = pytils.dt.ru_strftime(
            u"%B",
            inflected=False,
            date=duter_month,
        )
        # logging.debug(f'    {duter_month = }')
        duter_month = duter_month.capitalize()
        # logging.debug(f'    {duter_month = }')
        duter = (duter_month, duter_familia)
        # logging.debug(f'    {duter = }')
        duters_list.append(duter)
    now_duter = duters_list[now_month_n-1]
    # logging.debug(f'{now_duter = }')
    next_duter = duters_list[next_month_n-1]
    # logging.debug(f'{next_duter = }')
    if list:
        # logging.debug(f'if {list = }')
        # logging.debug(f'    {now_duter}, {next_duter}, {list}')
        return now_duter, next_duter, duters_list
    else:
        # logging.debug(f'else {list = }')
        # logging.debug(f'    {now_duter}, {next_duter}')
        return now_duter, next_duter

def iipp(request):
    x_forwardwd_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwardwd_for:
        ip = x_forwardwd_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def client_ip(request, pages):
    ip = iipp(request)
    vremya = datetime.datetime.now().replace(microsecond=0)
    print(f'ip = {vremya} - {ip}')
    if ip not in good_ips:
        for i in peoples:
            if i[2] == ip:
                posetitel = f'{i[1]} - {i[0]}'
                posesenie = f'{vremya} - {posetitel} - {pages}'
                print(f'posesenie = {posesenie}')
                break
            else:
                posesenie = f'{vremya} - Кто то неизвестный - {ip} - {pages}'
        try:
            stats = Static.objects.in_bulk()
            last = len(stats)
            now = last + 1
            Static.objects.get_or_create(id=now, log=posesenie)
            logging.info(f' {id} - {posesenie}')
            # Static.objects.get_or_create(log=posesenie)
            # logging.info(f' {id} - {posesenie}')
            # new_stats = request.POST.get('11111')
            # new_stats.save()
            ##### читаем базу данных ####
            # conn = sqlite3.connect(r'db.sqlite3')
            # cur = conn.cursor()
            # cur.execute("SELECT * FROM duty_static;")
            # all_stats = cur.fetchall()
            # logging.debug(f'{len(all_stats) = }')
            # logging.debug(f'{last = }')
            # last = stats[kolvo]
            # logging.debug(f'{ last = }')
            # id = len(all_stats) + 1
            # logs = [id, posesenie]
            #### добавляем в базу данных###
            # cur.execute("INSERT INTO duty_static VALUES(?,?);", logs)
            # conn.commit()
            # conn.close()
            # logging.info(f'[ {now} - {posesenie}')
        except:
            logging.error(f'{ip} - чет не то')
    else:
        logging.info(f'{vremya} - {ip} - {pages}')
    return

def name(ip):
    imya = ''
    for i in peoples:
        if ip in i:
            imya = i[0]
            break
        else:
            imya = 'error'
    return imya

def index(request):
    ip = iipp(request)
    now_month_n, now_month_ru, next_month_n,  next_month_ru = now_next_month()
    now_duter, next_duter = now_next_duter(now_month_n, next_month_n)
    now_day = datetime.datetime.now().day
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
    qr = reff(ip, qr_list)
    content = {
        'title': 'Расписание дежурств',
        'txt': 'Дежурства',
        'now': now_day,
        'now_month': now_month_n,
        'next': next_month_ru,
        'wtf': stroki,
        'ip': ip,
        'good_ips': good_ips,
        'now_duter': now_duter,
        'next_duter': next_duter,
        'qr': qr,
    }
    # logging.info(f'{ip = }')
    client_ip(request, content['title'])
    if ip not in bad_ip:
        return render(request, 'duty/index.html', content)
    else:
        return render(request, 'duty/index.html')

def edit_index(request):
    ip = iipp(request)
    now_month_n, now_month_ru, next_month_n,  next_month_ru = now_next_month()
    now_duter, next_duter = now_next_duter(now_month_n, next_month_n)
    now_day = datetime.datetime.now().day
    stroki = []
    wtf = Month.objects.in_bulk()
    imena = People.objects.in_bulk()
    surname = People.objects.all()
    for i in surname:
        logging.debug(f'{type(i.familia)} = {i.familia = }')
    for w in wtf:
        strochka = []
        d_n = wtf[w].day_of_week
        strochka.append(d_n)
        ch = wtf[w].id
        strochka.append(ch)
        id_d = wtf[w].person_id
        for im in imena:
            if imena[im].id == id_d:
                strochka.append(imena[im].familia)
        stroki.append(strochka)
    for s in stroki:
        logging.debug(f'{type(s[2]) = } - {s[2] = }')
    logging.debug(f'{surname = }')
    qr = reff(ip, qr_list)
    content = {
        'title': 'Расписание дежурств',
        'txt': 'Дежурства',
        'now': now_day,
        'now_month': now_month_n,
        'next': next_month_ru,
        'wtf': stroki,
        'ip': ip,
        'good_ips': good_ips,
        'now_duter': now_duter,
        'next_duter': next_duter,
        'qr': qr,
        'surname': surname,
    }
    # logging.info(f'{ip = }')
    client_ip(request, content['title'])
    if ip not in bad_ip:
        return render(request, 'duty/edit_index.html', content)
    else:
        return render(request, 'duty/edit_index.html')



def stat(request):
    now_month_n, now_month_ru, next_month_n, next_month_ru = now_next_month()
    now_duter, next_duter = now_next_duter(now_month_n, next_month_n)
    ip = iipp(request)
    if ip in good_ips:
        conn = sqlite3.connect(r'db.sqlite3')
        cur = conn.cursor()
        cur.execute("SELECT * FROM duty_static;")
        all_results = cur.fetchall()
        conn.close()
        title = 'Статистика'
    else:
        all_results = [['','Error 404'],[]]
        title = 'Error 404'
    all_results.reverse()
    content = {
        'title': title,
        'spisok' : all_results,
        # 'spisok' : all_results[-50:],
        'ip': ip,
        'hz': hashlib.sha1(b'{b}'),
        'good_ips': good_ips,
        'now_duter': now_duter,
        'next_duter': next_duter,
    }
    client_ip(request, content['title'])
    return render(request, 'duty/stat.html', content)

def news(request):
    ip = iipp(request)
    list = Article.objects.order_by('-pub_date')[:10]
    qr = reff(ip, qr_list)
    content = {
        'title': 'Новости',
        'ip': ip,
        'good_ips': good_ips,
        'test': list,
        'qr': qr,
    }
    client_ip(request, content['title'])
    return render(request, 'duty/news.html', content)

def otvet(request):
    logging.info(f'start open /otvetstven')
    now_month_n, now_month_ru, next_month_n,  next_month_ru = now_next_month()
    now_duter, next_duter, duters_list = now_next_duter(
        now_month_n,
        next_month_n,
        list=True
    )
    today = datetime.datetime.now()
    now = pytils.dt.ru_strftime(
        u"%B",
        inflected=False,
        date=today,
    )
    now = now.capitalize()
    ip = iipp(request)
    content = {
        'title': 'Ответственные дежурные',
        'ip': ip,
        'good_ips': good_ips,
        'now': now,
        'duters': duters_list,
        'now_duter': now_duter,
        'next_duter': next_duter,
    }
    client_ip(request, content['title'])
    return render(request, 'duty/otvet.html', content)

def rules(request):
    now_month_n, now_month_ru, next_month_n,  next_month_ru = now_next_month()
    now_duter, next_duter, duters_list = now_next_duter(
        now_month_n,
        next_month_n,
        list=True
    )
    ip = iipp(request)
    content = {
        'title': 'Положение о дежурстве',
        'ip': ip,
        'good_ips': good_ips,
        'now_duter': now_duter,
        'next_duter': next_duter,
    }
    client_ip(request, content['title'])
    return render(request, 'duty/rules.html', content)

def help(request):
    now_month_n, now_month_ru, next_month_n,  next_month_ru = now_next_month()
    now_duter, next_duter, duters_list = now_next_duter(
        now_month_n,
        next_month_n,
        list=True
    )
    ip = iipp(request)
    content = {
        'title': 'Справка',
        'ip': ip,
        'good_ips': good_ips,
        'now_duter': now_duter,
        'next_duter': next_duter,
    }
    if ip in ip_otv_de or ip in good_ips:
        content['password'] = 'raspisanie'
        content['tit'] = ''
    else:
        content['password'] = '*****'
        content['tit'] = 'Пароль только для ответственных дежурных'
    client_ip(request, content['title'])
    return render(request, 'duty/help.html', content)

def detail(request, article_id):
    ip = iipp(request)
    user = name(ip)
    try:
        ar = Article.objects.get(id=article_id)
    except:
        raise Http404('Статья не найдена')
    latest_comments_list = ar.comment_set.order_by('-id')[:10]
    qr = reff(ip, qr_list)
    content = {
        'article': ar,
        'latest_comments_list': latest_comments_list,
        'title': ar.article_title,
        'ip': ip,
        'hz': hashlib.sha1(ip.encode()).hexdigest(),
        'ips': peoples,
        'good_ips': good_ips,
        'user': user,
        'qr': qr,
    }
    print(content['hz'])
    client_ip(request, content['title'])
    return render(request, 'duty/detail.html', content)

def leave_comment(request, article_id):
    try:
        ar = Article.objects.get(id=article_id)
    except:
        raise Http404('Статья не найдена')
    ar.comment_set.create(
        author_name=request.POST['name'],
        comment_text=request.POST['text'],
        comment_ip=request.POST['send'],
    )
    return HttpResponseRedirect(reverse('detail', args=(ar.id,)))


# imena = People.objects.in_bulk()
