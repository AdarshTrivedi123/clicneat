# Generated by Django 4.2.3 on 2023-07-15 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clicknEat', '0002_wishlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='cart_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('p_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clicknEat.menu_data')),
            ],
        ),
    ]
