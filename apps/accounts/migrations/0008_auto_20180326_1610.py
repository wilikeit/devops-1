# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-03-26 08:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20180323_2142'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'default_permissions': (), 'permissions': (('get_user', '查看用户'), ('add_user', '添加用户'), ('edit_user', '编辑用户'), ('del_user', '删除用户')), 'verbose_name': '用户', 'verbose_name_plural': '用户'},
        ),
    ]
