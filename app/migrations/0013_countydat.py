# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-05-02 12:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_aboutl_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='CountyDat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('AvgAgeOlder', models.IntegerField(max_length=5)),
                ('AvgAgeYounger', models.IntegerField(max_length=5)),
                ('AvgBRChange', models.IntegerField(max_length=5)),
                ('MoreInfo', models.URLField(default='', max_length=1000)),
            ],
        ),
    ]
