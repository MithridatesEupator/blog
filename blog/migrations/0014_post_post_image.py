# Generated by Django 2.0.6 on 2018-06-25 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20180621_1958'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_image',
            field=models.FileField(blank=True, null=True, upload_to='images/%Y/%m/%D/'),
        ),
    ]
