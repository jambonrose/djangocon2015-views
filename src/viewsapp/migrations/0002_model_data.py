# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def add_data(apps, schema_editor):
    ExampleModel = apps.get_model('viewsapp', 'ExampleModel')
    ExampleModel.objects.create(
        name='django',
        slug='django')


def remove_data(apps, schema_editor):
    ExampleModel = apps.get_model('viewsapp', 'ExampleModel')
    ExampleModel.objects.filter(slug='django').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('viewsapp', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            add_data,
            reverse_code=remove_data),
    ]
