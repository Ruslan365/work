# Generated by Django 3.1.7 on 2021-06-01 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0019_auto_20210530_1239'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='preview_img',
            field=models.ImageField(blank=True, upload_to='post_preview_pics'),
        ),
    ]
