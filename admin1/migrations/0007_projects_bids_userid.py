# Generated by Django 3.1.5 on 2021-03-07 07:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('admin1', '0006_remove_projects_bids_userid'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects_bids',
            name='userid',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
