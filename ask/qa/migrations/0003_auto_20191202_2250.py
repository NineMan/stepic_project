# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-12-02 22:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0002_auto_20191112_2147'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ('added_at',)},
        ),
    ]
