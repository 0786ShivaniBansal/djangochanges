# Generated by Django 4.0 on 2022-01-07 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]