# Generated by Django 3.1.7 on 2021-08-14 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0027_auto_20210801_0938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(default='', max_length=30),
        ),
    ]
