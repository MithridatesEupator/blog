# Generated by Django 2.0.6 on 2018-07-04 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20180702_2008'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='bio',
            field=models.CharField(blank=True, max_length=240, null=True),
        ),
        migrations.AddField(
            model_name='myuser',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/profile/%Y/%m/%D/'),
        ),
    ]
