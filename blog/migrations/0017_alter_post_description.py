# Generated by Django 3.2.5 on 2021-08-05 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_post_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(verbose_name='توضیحات'),
        ),
    ]
