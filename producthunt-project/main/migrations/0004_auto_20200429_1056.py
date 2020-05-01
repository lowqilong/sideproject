# Generated by Django 2.1.5 on 2020-04-29 02:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200428_1714'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.AlterField(
            model_name='product',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 29, 10, 56, 17, 882552), verbose_name='date published'),
        ),
    ]
