# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_auto_20141229_1911'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('slug', models.SlugField()),
                ('tags', models.ManyToManyField(to='portfolio.Tag')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
