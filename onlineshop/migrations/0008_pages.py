# Generated by Django 3.1.2 on 2020-12-06 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineshop', '0007_auto_20201201_1659'),
    ]

    operations = [
        migrations.CreateModel(
            name='pages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Clothes', 'Clothes'), ('Accessory', 'Accessory'), ('Food', 'Food')], max_length=200, null=True)),
                ('product', models.CharField(max_length=200)),
            ],
        ),
    ]
