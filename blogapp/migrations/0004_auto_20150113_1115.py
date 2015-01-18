# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0003_post_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='_text_excerpt',
            field=models.TextField(editable=False, default='hello text'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=model_utils.fields.SplitField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
    ]
