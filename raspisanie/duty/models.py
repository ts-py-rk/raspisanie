from django.db import models


class People(models.Model):
    familia = models.CharField('Фамилия', max_length=10)
    imya = models.CharField('Имя', max_length=10)
    otche = models.CharField('Отчество', max_length=10)


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

        a = f'{self.person.familia} - {self.mesyas}'

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
    status = models.ForeignKey(Calendar, on_delete=models.CASCADE)
    day = models.DateField()
    day_of_week = models.CharField('День недели', max_length=10)
    person = models.ForeignKey(People, on_delete=models.CASCADE)
    super = models.ForeignKey(SuperDuty, on_delete=models.CASCADE)

    def __str__(self):
        if self.person == None:
            return "person IS NULL"

        a = f'{self.person.familia} - {self.day} - {self.day_of_week}'
        return a

    class Meta:
        verbose_name = "Дежурство"
        verbose_name_plural = "Дежурства"
