# Generated by Django 2.0.6 on 2018-06-26 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_text',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_text',
            field=models.TextField(default=''),
        ),
    ]
