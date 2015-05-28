# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20150528_0615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='runner',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 28, 6, 17, 48, 358545, tzinfo=utc), verbose_name=b'date published'),
            preserve_default=True,
        ),
    ]
