# Generated by Django 3.0.6 on 2020-10-02 03:11

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('princesswing', '0025_delete_catagary'),
    ]

    operations = [
        migrations.CreateModel(
            name='catagary',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Date1', models.DateTimeField(default=datetime.datetime(2020, 10, 2, 8, 41, 29, 432289))),
                ('Catagary', models.CharField(max_length=100, null=True)),
                ('Price', models.IntegerField(default='9999999999')),
                ('Qty', models.IntegerField(default='9999999999')),
                ('Image', models.ImageField(upload_to='images1/')),
                ('Discription', models.CharField(max_length=10000, null=True)),
                ('name', models.CharField(default='pad', max_length=10000, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
