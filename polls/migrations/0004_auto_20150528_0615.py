# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20150525_0533'),
    ]

    operations = [
        migrations.AddField(
            model_name='run',
            name='rgb',
            field=models.CharField(default=datetime.datetime(2015, 5, 28, 6, 15, 2, 182911, tzinfo=utc), max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='run',
            name='mood',
            field=models.CharField(max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='runner',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 28, 6, 14, 45, 673631, tzinfo=utc), verbose_name=b'date published'),
            preserve_default=True,
        ),
    ]
