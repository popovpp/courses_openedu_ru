# Generated by Django 3.0 on 2020-11-17 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labwork6', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='nameUnivercity',
            field=models.CharField(max_length=255, verbose_name='Название ВУЗа'),
        ),
    ]
