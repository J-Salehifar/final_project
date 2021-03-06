# Generated by Django 3.2.5 on 2021-08-04 13:44

import accounts.utils
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', django_jalali.db.models.jDateTimeField(auto_now_add=True, verbose_name='تاریخ عضویت')),
                ('age', models.PositiveSmallIntegerField(validators=[accounts.utils.check_is_digit], verbose_name='سن')),
                ('national_code', models.CharField(max_length=10, validators=[accounts.utils.check_is_digit], verbose_name='کد ملی')),
                ('mobile_number', models.CharField(max_length=11, validators=[accounts.utils.check_is_digit], verbose_name='تلفن همراه')),
                ('bio', models.TextField(blank=True, null=True, verbose_name='درباره من')),
                ('gender', models.CharField(choices=[('M', 'آقا'), ('F', 'خانم'), ('O', 'سایر')], max_length=1, verbose_name='جنسیت')),
                ('is_auther', models.BooleanField(default=False, verbose_name='نویسنده')),
                ('resumes', models.FileField(upload_to=accounts.utils.resume_file_path, verbose_name='رزومه')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'پروفایل',
                'verbose_name_plural': 'پروفایل ها',
            },
        ),
    ]
