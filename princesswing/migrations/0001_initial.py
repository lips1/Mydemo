# Generated by Django 3.0.6 on 2020-08-01 19:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('city', models.CharField(blank=True, max_length=100)),
                ('dob', models.DateField(blank=True, max_length=100)),
                ('gender', models.CharField(blank=True, max_length=100)),
                ('address', models.CharField(max_length=1000)),
            ],
        ),
    ]
