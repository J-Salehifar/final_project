# Generated by Django 3.2.5 on 2021-08-04 18:17

import blog.utils
from django.db import migrations, models
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_auther'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.PositiveSmallIntegerField(choices=[(1, 'در حال انتشار'), (2, 'عدم تایید'), (3, 'پیش نویس')], null=True, verbose_name='دسته بندی'),
        ),
        migrations.AddField(
            model_name='post',
            name='create_date',
            field=django_jalali.db.models.jDateTimeField(auto_now_add=True, null=True, verbose_name='تاریخ ایجاد'),
        ),
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.TextField(null=True, verbose_name='توضیحات'),
        ),
        migrations.AddField(
            model_name='post',
            name='edit_date',
            field=django_jalali.db.models.jDateTimeField(auto_now=True, verbose_name='تاریخ ویرایش'),
        ),
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.ImageField(height_field=100, null=True, upload_to=blog.utils.post_image_path, verbose_name='عکس', width_field=100),
        ),
        migrations.AddField(
            model_name='post',
            name='short_description',
            field=models.CharField(max_length=300, null=True, verbose_name='توضیحات خلاصه'),
        ),
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'در حال انتشار'), (2, 'عدم تایید'), (3, 'پیش نویس')], null=True, verbose_name='وضعیت'),
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=50, null=True, verbose_name='عنوان'),
        ),
    ]