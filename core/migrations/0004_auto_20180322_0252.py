# Generated by Django 2.0.3 on 2018-03-22 02:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20180322_0242'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blind',
            name='order',
        ),
        migrations.AddField(
            model_name='blind',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 22, 2, 52, 54, 567968, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='blind',
            name='ponumber',
            field=models.CharField(default='New Client', max_length=256),
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
