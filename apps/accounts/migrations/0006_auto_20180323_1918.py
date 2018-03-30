# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-03-23 11:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20180323_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_group',
            field=models.ManyToManyField(related_name='user_group', to='accounts.UserGroup', verbose_name='用户组'),
        ),
    ]
