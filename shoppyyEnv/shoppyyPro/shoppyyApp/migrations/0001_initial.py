# Generated by Django 5.1.1 on 2024-09-27 15:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=20)),
                ('product_price', models.TextField()),
                ('product_discription', models.TextField()),
                ('product_color', models.TextField()),
                ('product_quantity', models.TextField()),
                ('product_category', models.TextField()),
                ('product_image', models.FileField(upload_to='assets/product_image/')),
                ('product_date', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
