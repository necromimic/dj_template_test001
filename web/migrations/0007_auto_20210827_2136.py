# Generated by Django 3.2.5 on 2021-08-27 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_auto_20210822_1732'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
    ]
