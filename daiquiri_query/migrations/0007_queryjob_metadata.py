# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-16 14:17
from __future__ import unicode_literals

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('daiquiri_query', '0006_example'),
    ]

    operations = [
        migrations.AddField(
            model_name='queryjob',
            name='metadata',
            field=jsonfield.fields.JSONField(default={}),
            preserve_default=False,
        ),
    ]
