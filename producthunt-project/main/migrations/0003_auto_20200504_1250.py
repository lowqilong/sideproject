# Generated by Django 2.1.5 on 2020-05-04 04:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200503_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 4, 12, 50, 52, 722569), verbose_name='date published'),
        ),
    ]