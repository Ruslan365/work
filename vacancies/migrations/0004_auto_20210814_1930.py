# Generated by Django 3.1.7 on 2021-08-14 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0003_auto_20210814_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='Deadline',
            field=models.CharField(choices=[(0, 'Full Time'), (1, 'Part Time'), (2, 'Freelance')], max_length=300),
        ),
    ]