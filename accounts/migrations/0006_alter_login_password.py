# Generated by Django 4.0 on 2022-01-07 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_login_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='password',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
