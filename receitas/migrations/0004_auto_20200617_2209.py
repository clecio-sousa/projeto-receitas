# Generated by Django 3.0.6 on 2020-06-18 01:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0003_auto_20200617_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receita',
            name='data_receita',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 17, 22, 9, 9, 258584)),
        ),
    ]
