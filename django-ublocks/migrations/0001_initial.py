# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filebrowser.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('template', models.CharField(max_length=256, verbose_name=b'Template')),
            ],
            options={
                'verbose_name': 'Block',
                'verbose_name_plural': 'Blocks',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.SlugField(serialize=False, verbose_name=b'ID', primary_key=True)),
                ('title', models.CharField(max_length=128, null=True, verbose_name=b'Title', blank=True)),
                ('subtitle', models.CharField(max_length=256, null=True, verbose_name=b'Subtitle', blank=True)),
                ('text', models.TextField(null=True, verbose_name=b'Text', blank=True)),
                ('local_file', filebrowser.fields.FileBrowseField(max_length=256, null=True, verbose_name=b'Local File or image', blank=True)),
                ('url', models.URLField(null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Item',
                'verbose_name_plural': 'Items',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='block',
            name='item',
            field=models.ForeignKey(blank=True, to='django-ublocks.Item', null=True),
            preserve_default=True,
        ),
    ]
