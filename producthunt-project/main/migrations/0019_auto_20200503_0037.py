# Generated by Django 2.1.5 on 2020-05-02 16:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_auto_20200503_0033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 3, 0, 37, 42, 414582), verbose_name='date published'),
        ),
    ]