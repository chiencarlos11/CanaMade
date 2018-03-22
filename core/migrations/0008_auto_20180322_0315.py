# Generated by Django 2.0.3 on 2018-03-22 03:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20180322_0315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blind',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 22, 3, 15, 45, 401103, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='laurent',
            name='cassette',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='laurent',
            name='height',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='laurent',
            name='inner',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='laurent',
            name='outer',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='laurent',
            name='tube_bod',
            field=models.FloatField(blank=True, null=True),
        ),
    ]