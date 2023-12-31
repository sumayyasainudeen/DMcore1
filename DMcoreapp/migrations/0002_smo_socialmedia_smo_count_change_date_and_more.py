# Generated by Django 4.1.4 on 2023-07-24 06:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DMcoreapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='smo_socialmedia',
            name='smo_count_change_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='smo_socialmedia',
            name='smo_old_count',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='daily_leeds_exists',
            name='date',
            field=models.DateField(default=datetime.date(2023, 7, 24)),
        ),
    ]
