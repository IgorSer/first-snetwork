# Generated by Django 2.0 on 2018-02-11 03:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogging', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='birthday',
        ),
    ]
