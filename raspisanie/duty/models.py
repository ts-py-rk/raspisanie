from django.db import models


class People(models.Model):
    familia = models.CharField('Фамилия', max_length=10)
    imya = models.CharField('Имя', max_length=10)
    otche = models.CharField('Отчество', max_length=10)


class SuperDuty(models.Model):
    person = models.ForeignKey(People)
    month = models.DateField()
    year = models.DateField()


class Calendar(models.Model):
    day_of_year = models.CharField('День года', max_length=50)
    status = models.CharField('Статус', max_length=50)


class Month(models.Model):
    status = models.ForeignKey(Calendar)
    day = models.CharField('Название', max_length=50)
    day_of_week = models.CharField('День недели', max_length=50)
    person = models.ForeignKey(People)
    super = models.ForeignKey(SuperDuty)
