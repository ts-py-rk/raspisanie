# Generated by Django 3.1.5 on 2021-01-23 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('duty', '0003_delete_genre'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='month',
            options={'ordering': ('id',), 'verbose_name': 'Дежурства в этом месяце', 'verbose_name_plural': 'Дежурства в этом месяце'},
        ),
        migrations.AlterField(
            model_name='month',
            name='day_of_week',
            field=models.CharField(editable=False, max_length=10, verbose_name='День недели'),
        ),
        migrations.AlterField(
            model_name='month',
            name='status',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='duty.calendar'),
        ),
        migrations.AlterField(
            model_name='month',
            name='super',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='duty.superduty'),
        ),
        migrations.AlterField(
            model_name='people',
            name='familia',
            field=models.CharField(max_length=15, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='people',
            name='imya',
            field=models.CharField(max_length=15, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='people',
            name='otche',
            field=models.CharField(max_length=15, verbose_name='Отчество'),
        ),
    ]