# Generated by Django 2.1.5 on 2020-05-04 04:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200504_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 4, 12, 58, 43, 384221), verbose_name='date published'),
        ),
    ]
