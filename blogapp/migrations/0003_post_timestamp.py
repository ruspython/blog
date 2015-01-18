# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_auto_20150101_1150'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='timestamp',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 1, 3, 13, 27, 13, 552705)),
            preserve_default=False,
        ),
    ]
