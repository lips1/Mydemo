# Generated by Django 3.0.6 on 2020-09-15 12:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('princesswing', '0017_auto_20200915_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catagary',
            name='Date1',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 15, 17, 44, 47, 581702)),
        ),
    ]