# Generated by Django 2.0.6 on 2018-06-26 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_post_post_parent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post_Node',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Post_Tree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
