# -*- coding: utf-8 -*-
# Generated by Django 1.10a1 on 2016-06-19 17:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_auto_20160619_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventexcuse',
            name='description',
            field=models.TextField(verbose_name=b'I will not be attending None because'),
        ),
    ]