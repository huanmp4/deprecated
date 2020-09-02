# Generated by Django 3.0.3 on 2020-08-30 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('legendattach', '0004_allip_websitename'),
    ]

    operations = [
        migrations.CreateModel(
            name='legendSite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serverName', models.CharField(max_length=18)),
                ('ip', models.CharField(max_length=18)),
                ('time', models.DateTimeField()),
                ('type', models.CharField(max_length=18)),
                ('introduce', models.CharField(max_length=30)),
                ('QQ', models.CharField(max_length=18)),
                ('isActive', models.BooleanField(default=True)),
            ],
        ),
    ]
