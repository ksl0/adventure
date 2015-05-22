# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='run',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='run',
            name='run_date',
        ),
        migrations.AddField(
            model_name='runner',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 22, 21, 59, 58, 9225, tzinfo=utc), verbose_name=b'date published'),
            preserve_default=True,
        ),
    ]
