# Generated by Django 3.0.3 on 2020-08-31 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('legendattach', '0005_legendsite'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='legendsite',
            options={'ordering': ['time']},
        ),
        migrations.AlterField(
            model_name='legendsite',
            name='introduce',
            field=models.CharField(max_length=40),
        ),
    ]
