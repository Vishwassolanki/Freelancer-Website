# Generated by Django 3.0.6 on 2020-06-17 09:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user1', '0002_auto_20200615_1513'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_profile',
            name='userid',
        ),
    ]