# Generated by Django 3.1.7 on 2021-09-13 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0028_auto_20210814_0017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(blank=True, null=True, related_name='tags', to='posts.Tag'),
        ),
    ]
