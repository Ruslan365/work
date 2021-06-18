# Generated by Django 3.1.7 on 2021-05-01 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0013_post_author_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(blank=True, related_name='tags', to='posts.Tag'),
        ),
    ]
