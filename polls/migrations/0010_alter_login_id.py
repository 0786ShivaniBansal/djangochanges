# Generated by Django 4.0 on 2022-01-06 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_rename_password_login_password_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
