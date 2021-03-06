# Generated by Django 3.0.6 on 2020-08-02 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('princesswing', '0002_login'),
    ]

    operations = [
        migrations.CreateModel(
            name='loginform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserId', models.CharField(max_length=100, null=True)),
                ('EnterPassword', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='registrationform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserId', models.CharField(max_length=100, null=True)),
                ('EmailId', models.CharField(max_length=100, null=True)),
                ('Enterpassword', models.CharField(max_length=100, null=True)),
                ('Firstname', models.CharField(max_length=100, null=True)),
                ('Lastname', models.CharField(max_length=100, null=True)),
                ('Phone', models.IntegerField(max_length=100, null=True)),
                ('City', models.CharField(max_length=100, null=True)),
                ('Gender', models.CharField(max_length=100, null=True)),
                ('Address', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='login',
        ),
    ]
