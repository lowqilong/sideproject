# Generated by Django 2.1.5 on 2020-05-04 07:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20200504_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 4, 15, 31, 51, 689225), verbose_name='date published'),
        ),
    ]
