from django.shortcuts import render

def index(request):
    content = {
        'title': 'Расписание дежурств',
        'txt': 'Расписание дежурств',
    }
    return render(request, 'duty/index.html', content)