# Generated by Django 3.2.5 on 2021-09-08 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20210902_0201'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='resume',
        ),
    ]
