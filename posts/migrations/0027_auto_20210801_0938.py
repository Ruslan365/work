# Generated by Django 3.1.7 on 2021-08-01 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0026_post_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(default='', max_length=255),
        ),
    ]
