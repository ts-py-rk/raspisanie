import pytils
import hashlib
import logging
import sqlite3
import datetime
import requests
from .forms import MonthForm
from .models import Month
from .models import People
from .models import Static
from .models import Article
from .models import SuperDuty
from .commands import otdel
from .commands import month2
from django.urls import reverse
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect


# lvl = 10
lvl = 20
logging.basicConfig(
    filename='./log.log', level=lvl, format='%(levelname)s - %(message)s')


good_ips = [
    '172.41.0.174',         # Я
    '192.168.88.253',       # macbook
    '127.0.0.1',            # localhost
]
qr_list = [
    # '172.41.0.173',       # Скрипкин
    # '172.41.0.192',       # Шемякин
    # '172.41.0.174',       # Я


]
bad_ip = [
    # '172.41.0.174',  # Я
    '',
]
superduty_ip = [
    '172.41.0.174',     # я
    'свободное место'
]
peoples = otdel.peoples
mon_fro_bas = month2.month_from_base()
now_mon = month2.now_month()
month2.check(mon_fro_bas, now_mon)

def superduty():
    logging.debug(f'START superduty()')
    today = datetime.datetime.now().date().strftime('%y-%m')
    logging.debug(f'{today = }')
    for i in SuperDuty.objects.all():
        m = i.mesyas.strftime('%y-%m')
        if m == today:
            logging.debug(f'   {i = }')
            id = i.person_id
            logging.debug(f'   {id = }')
    s_d_now = People.objects.get(pk=id)
    logging.debug(f'   {s_d_now = }')
    logging.debug(f'   {s_d_now.ip = }')
    logging.debug(f'STOP superduty')
    return s_d_now.ip

def reff(ip, qr_list):
    if ip in qr_list:
        qr = 'on'
    else:
        qr = 'off'
    return qr

def now_next_month():
    logging.debug(f'start next_month():')
    today = datetime.datetime.now()
    logging.debug(f'    {today = }')
    now_month = today.month
    logging.debug(f'    {now_month = }')
    if now_month < 12:
        logging.debug(f'    now_month < 12:')
        next_month = now_month + 1
        logging.debug(f'        {next_month = }')
    else:
        logging.debug(f'    now_month >= 12:')
        next_month = 1
        logging.debug(f'        {next_month = }')
    date_next_month = datetime.date(today.year, next_month, 1)
    logging.debug(f'    {date_next_month = }')
    now_month_ru = pytils.dt.ru_strftime(
        u"%B",
        inflected=False,
        date=today
    )
    now_month_ru = now_month_ru.capitalize()
    logging.debug(f'    {now_month_ru = }')
    next_month_ru = pytils.dt.ru_strftime(
        u"%B",
        inflected=False,
        date=date_next_month
    )
    next_month_ru = next_month_ru.capitalize()
    logging.debug(f'    {next_month_ru = }')
    logging.debug(f'stop next_month()')
    return now_month, now_month_ru, next_month, next_month_ru

def now_next_duter(now_month_n, next_month_n, list=None):
    logging.debug(f'start now_next_duter({now_month_n}, {next_month_n}, {list}')
    imena = People.objects.in_bulk()
    logging.debug(f'{imena = }')
    duters = SuperDuty.objects.in_bulk()
    logging.debug(f'{duters = }')
    duters_list = []
    logging.debug(f'{duters_list = }')
    for id in duters:
        logging.debug(f'    {id = }')
        duter_id = duters[id].person_id
        logging.debug(f'    {duter_id = }')
        duter_familia = imena[duter_id].familia
        logging.debug(f'    {duter_familia = }')
        duter_month = duters[id].mesyas
        logging.debug(f'    {duter_month = }')
        duter_month = pytils.dt.ru_strftime(
            u"%B",
            inflected=False,
            date=duter_month,
        )
        logging.debug(f'    {duter_month = }')
        duter_month = duter_month.capitalize()
        logging.debug(f'    {duter_month = }')
        duter = (duter_month, duter_familia)
        logging.debug(f'    {duter = }')
        duters_list.append(duter)
    now_duter = duters_list[now_month_n-1]
    logging.debug(f'{now_duter = }')
    next_duter = duters_list[next_month_n-1]
    logging.debug(f'{next_duter = }')
    if list:
        logging.debug(f'if {list = }')
        logging.debug(f'    {now_duter}, {next_duter}, {list}')
        return now_duter, next_duter, duters_list
    else:
        logging.debug(f'else {list = }')
        logging.debug(f'    {now_duter}, {next_duter}')
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
        logging.debug(f'{posesenie = }')
        try:
            stats = Static.objects.in_bulk()
            logging.debug(f'{stats = }')
            last = len(stats)
            logging.debug(f'{last =}')
            now = last + 1
            while True:
                logging.debug(f'{now = }')
                objects_filter = Static.objects.filter(id=now)
                logging.debug(f'{ objects_filter = }')
                check = objects_filter.exists()
                logging.info(f'{check = }')
                if check:
                    logging.info(f'неудачная попытка записать статистику')
                    now += 1
                    continue
                else:
                    break
            Static.objects.get_or_create(id=now, log=posesenie)
            logging.info(f' {id} - {posesenie}')
            logging.info(f'[ {now} - {posesenie}')
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
        logging.debug(f'{ch = }')
        logging.debug(f'{type(ch) = }')
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
        'superduty_ip': superduty_ip
    }
    logging.info(f'{ip = }')
    client_ip(request, content['title'])
    if ip not in bad_ip:
        return render(request, 'duty/index.html', content)
    else:
        return render(request, 'duty/index.html')

def edit(request, month_id=None):
    error = ''
    if request.method == 'POST':
        logging.debug(f'{month_id = }')
        logging.debug(f'{request.method = }')
        form = MonthForm(request.POST)
        logging.debug(f'{form = }')
        logging.debug(f'{type(form) = }')
        logging.debug(f'{form.fields = }')
        logging.debug(f'{type(form.fields) = }')
        date_from_form = request.POST
        logging.debug(f'{date_from_form = }')
        edit_day_id = date_from_form["id"]
        new_duter = int(date_from_form["new_person"])
        logging.info(f'{new_duter = }')
        logging.debug(f'{ edit_day_id = }')
        if form.is_valid():
            logging.debug(f'form.is_valid()')
            logging.debug(f'{ edit_day_id = }')
            edit_day = Month.objects.get(pk=edit_day_id)
            logging.info(f'{edit_day = }')
            logging.warning(f'{edit_day.person_id = }')
            edit_day.person_id = new_duter
            logging.warning(f'{edit_day.person_id = }')
            edit_day.save()
            logging.warning(f'{edit_day.person_id = }')
            return redirect('edit')
        else:
            logging.error(f'{form.errors.as_data() = }')
            logging.error(f'АШЫПКА')
    else:
        form = MonthForm()

    ip = iipp(request)
    now_month_n, now_month_ru, next_month_n,  next_month_ru = now_next_month()
    now_duter, next_duter = now_next_duter(now_month_n, next_month_n)
    now_day = datetime.datetime.now().day
    stroki = []
    wtf = Month.objects.in_bulk()
    imena = People.objects.in_bulk()
    surname = People.objects.all()
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
    qr = reff(ip, qr_list)
    if ip in good_ips:
        title = f'Изменение дежурного {month_id} числа'
    else:
        title = f'Error 404 ({month_id})'
    content = {
        'title': title,
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
        'form': form,
        'month_id': month_id,
        'superduty_ip': superduty_ip
    }
    logging.info(f'{ip = }')
    client_ip(request, content['title'])
    if ip not in bad_ip:
        return render(request, 'duty/edit.html', content)
    else:
        return render(request, 'duty/edit.html')

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
        'spisok': all_results,
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
    logging.debug(f'start open /otvetstven')
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
    if ip in superduty_ip or ip in good_ips:
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
    latest_comments_list = ar.comment_set.order_by('-id')[:100]
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


superduty_now = superduty()
logging.debug(f'{superduty_ip = }')
superduty_ip[1] = superduty()
logging.debug(f'{superduty_ip = }')