# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-11-12 21:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='text',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='question',
            name='text',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='question',
            name='title',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterModelTable(
            name='answer',
            table='qa_answers',
        ),
        migrations.AlterModelTable(
            name='question',
            table='qa_questions',
        ),
    ]
