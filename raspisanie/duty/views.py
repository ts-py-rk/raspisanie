from django.shortcuts import render

def index(request):
    content = {
        'title': 'Расписание дежурств',
        'txt': 'просто текст',
    }
    return render(request, 'duty/index.html', content)