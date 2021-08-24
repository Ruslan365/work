# Generated by Django 3.1.7 on 2021-08-18 20:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('members', '0004_auto_20210818_2038'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='choices',
        ),
        migrations.AddField(
            model_name='group',
            name='choices',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]