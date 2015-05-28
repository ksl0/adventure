# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20150528_0617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='runner',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 28, 8, 18, 18, 906380, tzinfo=utc), verbose_name=b'date published'),
            preserve_default=True,
        ),
    ]
