# Generated by Django 4.0 on 2022-01-09 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_remove_web_details_web_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='web',
            name='number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]