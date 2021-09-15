# Generated by Django 3.2.5 on 2021-08-27 19:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0003_alter_profile_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='is_auther',
            field=models.BooleanField(default=False, verbose_name='نویسنده است؟'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profiles', to=settings.AUTH_USER_MODEL, verbose_name='کاربر'),
        ),
    ]