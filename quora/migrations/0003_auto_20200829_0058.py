# Generated by Django 3.1 on 2020-08-28 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quora', '0002_auto_20200828_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics/'),
        ),
    ]
