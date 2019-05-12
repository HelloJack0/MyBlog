# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-01-31 15:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddressInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='名称')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subs', to='api.AddressInfo', verbose_name='上级行政区划')),
            ],
            options={
                'verbose_name': '行政区划',
                'verbose_name_plural': '行政区划',
                'db_table': 'tb_areas',
            },
        ),
        migrations.CreateModel(
            name='ChinesePoems',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=150)),
                ('content', models.TextField()),
                ('author_id', models.IntegerField(verbose_name='作者ID')),
                ('dynasty', models.CharField(default='null', help_text='诗词所属年代， S-宋朝， T-唐朝', max_length=15, null=True)),
                ('author', models.CharField(max_length=150, verbose_name='作者')),
            ],
            options={
                'verbose_name': 'poems',
                'verbose_name_plural': 'poems',
                'db_table': 'tb_poems',
            },
        ),
        migrations.CreateModel(
            name='ChinesePoetry',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=150)),
                ('yunlv_rule', models.TextField()),
                ('author_id', models.IntegerField(verbose_name='作者ID')),
                ('content', models.TextField()),
                ('dynasty', models.CharField(default='null', help_text='诗词所属年代， S-宋朝， T-唐朝', max_length=20, null=True)),
                ('author', models.CharField(max_length=150, verbose_name='作者')),
            ],
            options={
                'verbose_name': 'poetry',
                'verbose_name_plural': 'poetry',
                'db_table': 'tb_poetry',
            },
        ),
        migrations.CreateModel(
            name='ChineseUniversity',
            fields=[
                ('id', models.IntegerField(auto_created=True)),
                ('sid', models.IntegerField(help_text='school_id')),
                ('cid', models.IntegerField(help_text='city_id')),
                ('name', models.CharField(max_length=255, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': '学校',
                'verbose_name_plural': '学校',
                'db_table': 'school',
            },
        ),
        migrations.CreateModel(
            name='DetailAddressInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='名称')),
                ('ddd', models.IntegerField(blank=True, null=True, verbose_name='长途区号')),
                ('post_code', models.IntegerField(blank=True, null=True, verbose_name='邮政编码')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subs', to='api.DetailAddressInfo', verbose_name='上级行政+区划')),
            ],
            options={
                'verbose_name': '详细行政区划',
                'verbose_name_plural': '详细行政区划',
                'db_table': 'tb_areas_detail',
            },
        ),
        migrations.CreateModel(
            name='PoemsAuthors',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('intro_l', models.TextField()),
                ('intro_s', models.TextField()),
                ('dynasty', models.CharField(default='null', help_text=' S-宋朝， T-唐朝', max_length=15, null=True)),
            ],
            options={
                'verbose_name': 'poems_author',
                'verbose_name_plural': 'poems_author',
                'db_table': 'tb_poems_author',
            },
        ),
        migrations.CreateModel(
            name='PoetryAuthors',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('intro', models.TextField()),
                ('dynasty', models.CharField(default='null', help_text=' S-宋朝， T-唐朝', max_length=15, null=True)),
            ],
            options={
                'verbose_name': 'poetry_author',
                'verbose_name_plural': 'poetry_author',
                'db_table': 'tb_poetry_author',
            },
        ),
        migrations.CreateModel(
            name='RelationPoems',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.PoemsAuthors', verbose_name='作者')),
                ('poems', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.RelationPoems', verbose_name='作品')),
            ],
            options={
                'verbose_name': 'peoms_relation',
                'verbose_name_plural': 'peoms_relation',
                'db_table': 'tb_peoms_relation',
            },
        ),
        migrations.CreateModel(
            name='UniversityDepartment',
            fields=[
                ('id', models.IntegerField(auto_created=True)),
                ('sid', models.IntegerField(help_text='school_id')),
                ('did', models.IntegerField(help_text='department_id')),
                ('name', models.CharField(max_length=255, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': '院系',
                'verbose_name_plural': '院系',
                'db_table': 'department',
            },
        ),
    ]
