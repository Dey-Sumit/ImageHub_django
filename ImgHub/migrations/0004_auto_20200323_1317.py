# Generated by Django 2.2 on 2020-03-23 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ImgHub', '0003_auto_20200307_2030'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagedb',
            name='hash_val',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='imagedb',
            name='v_ctg',
            field=models.CharField(default='unknown', max_length=10),
        ),
    ]
