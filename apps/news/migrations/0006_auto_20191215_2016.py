# Generated by Django 2.0 on 2019-12-15 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_remove_discover_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='pub_time2',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='pub_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
