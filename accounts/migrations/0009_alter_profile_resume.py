# Generated by Django 3.2.5 on 2021-09-09 01:04

import accounts.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_profile_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='resume',
            field=models.FileField(blank=True, default=None, upload_to=accounts.utils.resume_file_path, verbose_name='رزومه'),
        ),
    ]
