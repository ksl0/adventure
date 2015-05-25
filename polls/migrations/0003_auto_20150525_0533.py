# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20150522_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='runner',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 25, 5, 33, 26, 360676, tzinfo=utc), verbose_name=b'date published'),
            preserve_default=True,
        ),
    ]
