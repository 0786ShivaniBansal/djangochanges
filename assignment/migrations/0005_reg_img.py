# Generated by Django 4.0.1 on 2022-01-20 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0004_rename_username_login_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='reg',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='img'),
        ),
    ]
