# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-13 17:27
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('estore', '0004_auto_20170813_1708'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='token',
            field=models.UUIDField(db_index=True, default=uuid.uuid4),
        ),
    ]
