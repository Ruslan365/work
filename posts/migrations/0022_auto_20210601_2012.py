# Generated by Django 3.1.7 on 2021-06-01 20:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0021_remove_post_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='preview_img',
            new_name='preview_pic',
        ),
    ]