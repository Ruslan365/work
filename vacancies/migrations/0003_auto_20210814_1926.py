# Generated by Django 3.1.7 on 2021-08-14 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0002_auto_20210814_0017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='Deadline',
            field=models.CharField(choices=[('Full Time', 'Full Time'), ('Part Time', 'Part Time'), ('Freelance', 'Freelance')], max_length=300),
        ),
    ]
