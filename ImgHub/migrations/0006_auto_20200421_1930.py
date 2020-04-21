# Generated by Django 2.2 on 2020-04-21 14:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ImgHub', '0005_auto_20200421_1829'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagedb',
            name='caption',
            field=models.TextField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='imagedb',
            name='published_on',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 21, 14, 0, 8, 809305, tzinfo=utc)),
        ),
    ]