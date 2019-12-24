# Generated by Django 2.0 on 2019-12-24 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0002_auto_20191223_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(default='null', max_length=10),
        ),
        migrations.AlterField(
            model_name='address',
            name='content',
            field=models.CharField(default='null', max_length=20),
        ),
        migrations.AlterField(
            model_name='address',
            name='country',
            field=models.CharField(default='null', max_length=10),
        ),
        migrations.AlterField(
            model_name='address',
            name='isp',
            field=models.CharField(default='null', max_length=10),
        ),
        migrations.AlterField(
            model_name='address',
            name='province',
            field=models.CharField(default='null', max_length=10),
        ),
    ]