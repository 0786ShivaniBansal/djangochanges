# Generated by Django 4.0 on 2022-01-05 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_login'),
    ]

    operations = [
        migrations.RenameField(
            model_name='login',
            old_name='Password',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='login',
            old_name='Username',
            new_name='username',
        ),
    ]