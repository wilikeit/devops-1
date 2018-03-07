# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-03-06 16:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0015_auto_20180307_0019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idc',
            name='manage_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='管理人'),
        ),
    ]