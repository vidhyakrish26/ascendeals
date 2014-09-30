# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20140929_0717'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='coupon',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
