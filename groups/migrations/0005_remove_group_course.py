# Generated by Django 2.2 on 2019-04-18 22:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0004_merge_20190418_2224'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='course',
        ),
    ]