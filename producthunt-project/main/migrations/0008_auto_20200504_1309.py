# Generated by Django 2.1.5 on 2020-05-04 05:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20200504_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 4, 13, 9, 0, 590038), verbose_name='date published'),
        ),
    ]
