# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-02-01 23:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20190201_2138'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_down',
            field=models.IntegerField(default=0, verbose_name='踩'),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_like',
            field=models.IntegerField(default=0, verbose_name='顶'),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_support',
            field=models.CharField(choices=[('1', '推荐'), ('0', '取消推荐')], default='1', max_length=10, verbose_name='文章推荐'),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_up',
            field=models.CharField(choices=[('1', '置顶'), ('0', '取消置顶')], default='1', max_length=10, verbose_name='文章置顶'),
        ),
    ]
