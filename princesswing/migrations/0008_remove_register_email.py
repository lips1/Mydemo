# Generated by Django 3.0.6 on 2020-08-14 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('princesswing', '0007_register_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='email',
        ),
    ]
