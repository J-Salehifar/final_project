# Generated by Django 3.2.5 on 2021-08-04 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_profile_age'),
        ('blog', '0002_auto_20210804_1755'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='auther',
            field=models.ManyToManyField(blank=True, related_name='posts', to='accounts.Profile', verbose_name='نویسنده'),
        ),
    ]