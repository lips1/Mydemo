# Generated by Django 3.0.6 on 2020-09-15 12:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('princesswing', '0016_auto_20200915_1734'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catagary',
            name='Date',
        ),
        migrations.AddField(
            model_name='catagary',
            name='Date1',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 15, 17, 38, 53, 11289)),
        ),
    ]
