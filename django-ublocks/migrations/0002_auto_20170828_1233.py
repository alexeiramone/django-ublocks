# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django-ublocks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='id',
            field=models.SlugField(primary_key=True, serialize=False, max_length=128, help_text='Slug, should be unique', verbose_name=b'ID'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='local_file',
            field=models.FileField(max_length=256, upload_to=b'', null=True, verbose_name=b'Local File or image', blank=True),
            preserve_default=True,
        ),
    ]
