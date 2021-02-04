from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('stat', views.stat, name='statistics'),
    path('otvet', views.otvet, name='otv'),
    path('news', views.news, name='news'),
    path('rules', views.rules, name='rules'),
    path('help', views.help, name='help'),
]