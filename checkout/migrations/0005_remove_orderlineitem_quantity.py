# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-04-18 15:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_orderlineitem_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderlineitem',
            name='quantity',
        ),
    ]
