# Generated by Django 3.2.5 on 2021-08-05 02:47

from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_profile_age'),
        ('blog', '0020_post_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'پست', 'verbose_name_plural': 'پست ها'},
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', django_jalali.db.models.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('budy', models.TextField(verbose_name='متن دیدگاه')),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'در حال انتشار'), (2, 'عدم تایید'), (3, 'پیش نویس')], default=3, verbose_name='وضعیت')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.post', verbose_name='پست')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comments', to='accounts.profile', verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'دیدگاه',
                'verbose_name_plural': 'دیدگاه ها',
            },
        ),
    ]