# Generated by Django 3.1.7 on 2021-04-29 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210429_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]
