# Generated by Django 3.1.7 on 2021-05-05 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20210501_1402'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='role',
            options={'ordering': ['name']},
        ),
        migrations.RemoveField(
            model_name='role',
            name='level',
        ),
        migrations.RemoveField(
            model_name='role',
            name='lft',
        ),
        migrations.RemoveField(
            model_name='role',
            name='rght',
        ),
        migrations.RemoveField(
            model_name='role',
            name='tree_id',
        ),
        migrations.AlterField(
            model_name='role',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='users.role'),
        ),
    ]
