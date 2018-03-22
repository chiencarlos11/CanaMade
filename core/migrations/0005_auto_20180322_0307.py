# Generated by Django 2.0.3 on 2018-03-22 03:07

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20180322_0252'),
    ]

    operations = [
        migrations.CreateModel(
            name='ControlPosition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ControlType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='blind',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 22, 3, 6, 55, 952693, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='laurent',
            name='control_position',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.DO_NOTHING, to='core.ControlPosition'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='laurent',
            name='control_type',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.DO_NOTHING, to='core.ControlType'),
            preserve_default=False,
        ),
    ]