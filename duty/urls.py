from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('stat', views.stat, name='statistics'),
    path('otvetstven', views.otvet, name='otv'),
    path('news', views.news, name='news'),
    path('rules', views.rules, name='rules'),
    path('help', views.help, name='help'),
    path('<int:article_id>/', views.detail, name='detail'),
    path('<int:article_id>/leave_comment/', views.leave_comment, name='leave_comment'),
    path('edit_index', views.edit_index, name='edit_index'),
]


