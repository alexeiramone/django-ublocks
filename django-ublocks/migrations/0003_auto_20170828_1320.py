# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('django-ublocks', '0002_auto_20170828_1233'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ['id'], 'verbose_name': 'Item', 'verbose_name_plural': 'Items'},
        ),
        migrations.AddField(
            model_name='block',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 28, 16, 19, 48, 561000, tzinfo=utc), verbose_name=b'Date Created', auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='block',
            name='date_updated',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 28, 16, 19, 58, 633000, tzinfo=utc), auto_now=True, auto_now_add=True, verbose_name=b'Date Last Updated'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 28, 16, 20, 8, 61000, tzinfo=utc), verbose_name=b'Date Created', auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='date_updated',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 28, 16, 20, 11, 533000, tzinfo=utc), auto_now=True, auto_now_add=True, verbose_name=b'Date Last Updated'),
            preserve_default=False,
        ),
    ]
