# Generated by Django 2.0.3 on 2018-03-23 01:29

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20180322_0315'),
    ]

    operations = [
        migrations.CreateModel(
            name='FabricType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='laurent',
            name='fabric_color',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.DO_NOTHING, to='core.FabricColor'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blind',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 23, 1, 28, 9, 658753, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='laurent',
            name='fabric',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Fabric'),
        ),
        migrations.AddField(
            model_name='fabric',
            name='fabric',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.DO_NOTHING, to='core.FabricType'),
            preserve_default=False,
        ),
    ]
