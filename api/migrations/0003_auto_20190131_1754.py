# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-01-31 17:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20190131_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addressinfo',
            name='code',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='城乡分类代码'),
        ),
    ]
