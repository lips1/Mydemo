# Generated by Django 3.1.2 on 2020-10-24 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('princesswing', '0038_auto_20201012_1840'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catagary',
            name='user',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='user',
        ),
        migrations.RemoveField(
            model_name='order',
            name='ID',
        ),
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.RemoveField(
            model_name='reg1',
            name='user',
        ),
        migrations.DeleteModel(
            name='cart',
        ),
        migrations.DeleteModel(
            name='catagary',
        ),
        migrations.DeleteModel(
            name='contact',
        ),
        migrations.DeleteModel(
            name='order',
        ),
        migrations.DeleteModel(
            name='reg1',
        ),
    ]
