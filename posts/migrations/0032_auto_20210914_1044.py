# Generated by Django 3.1.7 on 2021-09-14 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0031_auto_20210914_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(default=None, null=True, related_name='tags', to='posts.Tag'),
        ),
    ]