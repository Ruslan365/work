# Generated by Django 3.1.7 on 2021-08-14 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='work',
            old_name='role',
            new_name='Deadline',
        ),
        migrations.AddField(
            model_name='work',
            name='Location',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='work',
            name='Position',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='work',
            name='Salary',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]