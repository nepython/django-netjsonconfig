# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-11 15:33

import collections
import jsonfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_netjsonconfig', '0003_config_last_ip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='config',
            name='config',
            field=jsonfield.fields.JSONField(blank=True, dump_kwargs={'indent': 4}, default=dict, help_text='configuration in NetJSON DeviceConfiguration format', load_kwargs={'object_pairs_hook': collections.OrderedDict}, verbose_name='configuration'),
        ),
    ]
