# Generated by Django 3.0.6 on 2020-06-04 22:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0015_auto_20200605_0031'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='film',
            name='category',
        ),
        migrations.RemoveField(
            model_name='series',
            name='category',
        ),
    ]
