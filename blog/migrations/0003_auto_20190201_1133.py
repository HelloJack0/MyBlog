# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-02-01 11:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190201_1107'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='imagecategory',
            options={'verbose_name': '图片分类', 'verbose_name_plural': '图片分类'},
        ),
    ]
