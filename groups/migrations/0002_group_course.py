# Generated by Django 2.2 on 2019-04-18 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='course',
            field=models.CharField(default='yeet', max_length=200),
            preserve_default=False,
        ),
    ]
