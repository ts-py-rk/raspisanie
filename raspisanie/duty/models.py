from django.db import models
from django.utils import timezone
import datetime


class People(models.Model):
    familia = models.CharField('Фамилия', max_length=15)
    imya = models.CharField('Имя', max_length=15)
    otche = models.CharField('Отчество', max_length=15)

    def __str__(self):
        if self.familia == None:
            return "familia IS NULL"
        return self.familia

    class Meta:
        verbose_name = "Сотрудник отдела 41"
        verbose_name_plural = "Сотрудники отдела 41"


class SuperDuty(models.Model):
    person = models.ForeignKey(People, on_delete=models.CASCADE)
    mesyas = models.DateField()
    year = models.DateField()

    def __str__(self):
        if self.person == None:
            return "person IS NULL"
        a = f'{self.mesyas} - {self.person.familia}'
        return a

    class Meta:
        verbose_name = "Ответственный дежурный"
        verbose_name_plural = "Ответственные дежурные"


class Calendar(models.Model):
    day_of_year = models.CharField('День года', max_length=50)
    status = models.CharField('Статус', max_length=50)

    def __str__(self):
        if self.day_of_year == None:
            return "day_of_year IS NULL"
        return self.day_of_year

    class Meta:
        verbose_name = "День в году"
        verbose_name_plural = "Дни в году"


class Month(models.Model):
    status = models.ForeignKey(Calendar, on_delete=models.CASCADE, editable=False)
    day = models.DateField()
    day_of_week = models.CharField('День недели', max_length=10, editable=False)
    person = models.ForeignKey(People, on_delete=models.CASCADE)
    super = models.ForeignKey(SuperDuty, on_delete=models.CASCADE, editable=False)

    def __str__(self):
        if self.person == None:
            return "person IS NULL"
        d_o_w = self.day_of_week
        chislo = str(self.day.day)
        name = self.person.familia
        a = f'{d_o_w}  - {chislo} - {name}'
        return a

    class Meta:
        verbose_name = "Дежурства в этом месяце"
        verbose_name_plural = "Дежурства в этом месяце"
        ordering = ('id',)


class Static(models.Model):
    log = models.CharField('Посещение', max_length=100)

    def __str__(self):
        if self.log == None:
            return "log IS NULL"
        return self.log

    class Meta:
        verbose_name = "Запись посещения"
        verbose_name_plural = "Записи посещений"




class Article(models.Model):
    article_title = models.CharField('название статьи', max_length=200)
    article_text = models.TextField('текст статьи')
    pub_date = models.DateTimeField('дата публикации')

    def __str__(self):
        return self.article_title

    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days=7))

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author_name = models.CharField('имя', max_length=50)
    comment_text = models.CharField('текст коментария', max_length=200)
    comment_ip = models.CharField('ip', max_length=20)

    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'