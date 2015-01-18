# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_project_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='snapshot',
            field=models.ImageField(upload_to='portfolio/images'),
            preserve_default=True,
        ),
    ]
