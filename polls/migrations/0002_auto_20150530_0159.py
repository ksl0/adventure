# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='run',
            name='position',
        ),
        migrations.AddField(
            model_name='run',
            name='location',
            field=geoposition.fields.GeopositionField(max_length=42, null=True),
            preserve_default=True,
        ),
    ]
