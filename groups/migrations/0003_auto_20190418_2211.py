# Generated by Django 2.1.7 on 2019-04-18 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_auto_20190418_2115'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=255)),
                ('user_course', models.CharField(blank=True, max_length=255, null=True)),
                ('user_primary_language', models.CharField(max_length=255)),
                ('user_secondary_language', models.CharField(blank=True, max_length=255, null=True)),
                ('user_preferred_time', models.IntegerField()),
                ('user_preferred_day', models.IntegerField()),
                ('user_preferred_location', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='group',
            name='group_primary_lanuage',
        ),
        migrations.RemoveField(
            model_name='group',
            name='group_secondary_lanuage',
        ),
        migrations.AddField(
            model_name='group',
            name='group_primary_language',
            field=models.CharField(default='English', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='group',
            name='group_secondary_language',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='group',
            name='group_course',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='group',
            name='group_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='group',
            name='meeting_location',
            field=models.CharField(max_length=255),
        ),
    ]
