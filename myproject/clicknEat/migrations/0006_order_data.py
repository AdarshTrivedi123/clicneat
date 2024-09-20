# Generated by Django 4.2.3 on 2023-07-23 07:11

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clicknEat', '0005_alter_cart_data_qty'),
    ]

    operations = [
        migrations.CreateModel(
            name='order_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('qty', models.IntegerField(default=1)),
                ('date_time', models.DateTimeField(default=datetime.datetime(2023, 7, 23, 12, 41, 1, 273442))),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('p_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clicknEat.menu_data')),
            ],
        ),
    ]
