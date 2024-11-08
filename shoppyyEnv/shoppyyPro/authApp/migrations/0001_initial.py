# Generated by Django 5.1.1 on 2024-09-26 15:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registeruser',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.TextField()),
                ('mobileno', models.CharField(max_length=10)),
                ('image', models.FileField(upload_to='assets/image/')),
                ('usertype', models.TextField(default='user')),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
