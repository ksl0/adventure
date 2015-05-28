# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_auto_20150528_0820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='runner',
            name='start_date',
            field=models.DateTimeField(auto_now=True, verbose_name=b'date published'),
            preserve_default=True,
        ),
    ]
