# Generated by Django 4.0 on 2022-01-09 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_alter_web_num'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='web',
            name='num',
        ),
    ]