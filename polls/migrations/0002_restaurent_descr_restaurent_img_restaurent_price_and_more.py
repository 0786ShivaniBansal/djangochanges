# Generated by Django 4.0 on 2022-01-02 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurent',
            name='descr',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='restaurent',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='img'),
        ),
        migrations.AddField(
            model_name='restaurent',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='restaurent',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='restaurent',
            name='offer',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
