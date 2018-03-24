# Generated by Django 2.0.3 on 2018-03-23 01:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20180323_0136'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fabric',
            name='fabric_type',
        ),
        migrations.AlterField(
            model_name='blind',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 23, 1, 46, 49, 611000, tzinfo=utc)),
        ),
        migrations.DeleteModel(
            name='FabricType',
        ),
    ]