# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('eid', models.IntegerField()),
                ('ename', models.CharField(max_length=50, blank=True)),
                ('created_by', models.CharField(max_length=50)),
                ('updated_by', models.CharField(max_length=50, null=True, blank=True)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_on', models.DateTimeField(null=True, blank=True)),
                ('is_deleted', models.BooleanField(default=False, choices=[(True, True), (False, False)])),
            ],
        ),
        migrations.CreateModel(
            name='salary',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sid', models.IntegerField()),
                ('salary', models.FloatField(max_length=50, blank=True)),
                ('created_by', models.CharField(max_length=50)),
                ('updated_by', models.CharField(max_length=50, null=True, blank=True)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_on', models.DateTimeField(null=True, blank=True)),
                ('info', models.ForeignKey(blank=True, to='emp.info', null=True)),
            ],
        ),
    ]
