# Generated by Django 3.2.5 on 2021-08-05 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_post_short_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='short_description',
            field=models.CharField(max_length=300, verbose_name='توضیحات خلاصه'),
        ),
    ]
