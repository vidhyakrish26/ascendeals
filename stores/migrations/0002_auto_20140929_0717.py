# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20140929_0717'),
        ('stores', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='storecategory',
            name='category',
        ),
        migrations.RemoveField(
            model_name='storecategory',
            name='store',
        ),
        migrations.DeleteModel(
            name='StoreCategory',
        ),
    ]
