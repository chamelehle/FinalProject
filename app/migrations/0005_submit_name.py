# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-04-11 14:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20170305_1157'),
    ]

    operations = [
        migrations.AddField(
            model_name='submit',
            name='name',
            field=models.CharField(default=0, max_length=250),
            preserve_default=False,
        ),
    ]
