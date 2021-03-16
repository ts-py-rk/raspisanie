from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Article
import datetime
import pytils
from .models import Month
from .models import People
from .ips import a
import sqlite3
import hashlib

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
ip_otv_de = [
    '172.41.0.167',     # Рябин
]

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
        for i in a:
            if i[2] == ip:
                posetitel = f'{i[1]} - {i[0]}'
                posesenie = f'{vremya} - {posetitel} - {pages}'
                print(f'posesenie = {posesenie}')
                break
            else:
                posesenie = f'{vremya} - Кто то неизвестный - {ip} - {pages}'
        ##### читаем базу данных ####
        conn = sqlite3.connect(r'db.sqlite3')
        cur = conn.cursor()
        cur.execute("SELECT * FROM duty_static;")
        id = int(datetime.datetime.now().timestamp()) - 1611679693
        logs = [id, posesenie]
        #### добавляем в базу данных###
        cur.execute("INSERT INTO duty_static VALUES(?,?);", logs)
        conn.commit()
        conn.close()
    return

def name(ip):
    for i in a:
        if ip in i:
            imya = i[0]
            break
        else:
            imya = 'error'
    return imya

def index(request):
    ip = iipp(request)
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
        'ip': ip,
        'good_ips': good_ips,
    }
    client_ip(request, content['title'])
    return render(request, 'duty/index.html', content)

def stat(request):
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
    }
    client_ip(request, content['title'])
    return render(request, 'duty/stat.html', content)

def news(request):
    ip = iipp(request)
    list = Article.objects.order_by('-pub_date')[:5]

    content = {
        'title': 'Новости',
        'ip': ip,
        'good_ips': good_ips,
        'test': list,
    }

    client_ip(request, content['title'])
    return render(request, 'duty/news.html', content)

def otvet(request):
    ip = iipp(request)
    content = {
        'title': 'Ответственные дежурные',
        'ip': ip,
        'good_ips': good_ips,
    }
    client_ip(request, content['title'])
    return render(request, 'duty/otvet.html', content)

def rules(request):
    ip = iipp(request)
    content = {
        'title': 'Положение о дежурстве',
        'ip': ip,
        'good_ips': good_ips,
    }
    client_ip(request, content['title'])
    return render(request, 'duty/rules.html', content)

def help(request):
    ip = iipp(request)
    content = {
        'title': 'Справка',
        'ip': ip,
        'good_ips': good_ips,
    }
    if ip in ip_otv_de or ip in good_ips:
        content['password'] = 'raspisanie'
        content['tit'] = ''
    else:
        content['password'] = '*****'
        content['tit'] = 'Пароль только для ответственных дежурных'
    client_ip(request, content['title'])
    return render(request, 'duty/help.html', content)
#
def detail(request, article_id):
    ip = iipp(request)
    user = name(ip)
    try:
        ar = Article.objects.get(id = article_id)
    except:
        raise Http404('Статья не найдена')
    latest_comments_list = ar.comment_set.order_by('-id')[:10]
    content = {
        'article': ar,
        'latest_comments_list': latest_comments_list,
        'title': ar.article_title,
        'ip': ip,
        'hz': hashlib.sha1(ip.encode()).hexdigest(),
        'ips': a,
        'good_ips': good_ips,
        'user': user,
    }
    print(content['hz'])
    client_ip(request, content['title'])
    return render(request, 'duty/detail.html', content)

# def detail(request, article_id):
#     ip = iipp(request)
#     user = name(ip)
#     try:
#         ar = Article.objects.get(id = article_id)
#     except:
#         raise Http404('Статья не найдена')
#     latest_comments_list = ar.comment_set.order_by('-id')[:10]
#     content = {
#         'article': ar,
#         'latest_comments_list': latest_comments_list,
#         'title': ar.article_title,
#         'ip': ip,
#         'hz': hashlib.sha1(b'{ip}'),
#         'ips': a,
#         'good_ips': good_ips,
#         'user': user,
#     }
#     client_ip(request, content['title'])
#     return render(request, 'duty/detail.html', content)

def leave_comment(request, article_id):
    try:
        ar = Article.objects.get(id=article_id)
    except:
        raise Http404('Статья не найдена')

    ar.comment_set.create(author_name = request.POST['name'], comment_text = request.POST['text'], comment_ip = request.POST['send'])

    return HttpResponseRedirect(reverse('detail', args=(ar.id,)))