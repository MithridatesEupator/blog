# Generated by Django 2.0.6 on 2018-06-21 23:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20180621_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 6, 21, 19, 50, 37, 181245)),
        ),
    ]
