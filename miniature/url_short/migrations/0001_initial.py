# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField(unique=True)),
                ('short_url', models.CharField(max_length=16, blank=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
