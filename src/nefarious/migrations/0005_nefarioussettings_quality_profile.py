# Generated by Django 2.1.1 on 2018-11-30 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nefarious', '0004_auto_20181116_2326'),
    ]

    operations = [
        migrations.AddField(
            model_name='nefarioussettings',
            name='quality_profile',
            field=models.CharField(default='hd-720p-1080p', max_length=500),
        ),
    ]
