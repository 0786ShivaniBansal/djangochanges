# Generated by Django 4.0.1 on 2022-01-26 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0004_userdetails'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdetails',
            old_name='idname',
            new_name='userid',
        ),
    ]
