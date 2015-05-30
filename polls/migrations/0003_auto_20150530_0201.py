# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import geoposition.fields
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20150530_0159'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='run',
            name='location',
        ),
        migrations.AddField(
            model_name='run',
            name='position',
            field=geoposition.fields.GeopositionField(default=datetime.datetime(2015, 5, 30, 2, 1, 51, 541145, tzinfo=utc), max_length=42),
            preserve_default=False,
        ),
    ]
