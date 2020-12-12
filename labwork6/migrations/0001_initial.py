# Generated by Django 3.0 on 2020-11-17 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('idCourse', models.CharField(max_length=10, verbose_name='Идентификатор курса')),
                ('nameCourse', models.CharField(max_length=120, verbose_name='Наименование курса')),
                ('urlCourse', models.CharField(max_length=255, verbose_name='Адрес страницы курса')),
                ('descriptionCourse', models.TextField(verbose_name='Описание курса')),
                ('nameUnivercity', models.TextField(verbose_name='Название ВУЗа')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Дата получения информации')),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
                'db_table': 'courses',
                'ordering': ['idCourse'],
            },
        ),
    ]
