# Generated by Django 3.1.5 on 2021-03-07 09:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hirer', '0004_auto_20200302_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post_job',
            name='userid',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
