# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-05-02 22:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_countydat_geom'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CountyDat',
        ),
    ]
