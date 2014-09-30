# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0002_auto_20140929_0717'),
        ('catalogs', '0002_category_stores'),
        ('products', '0003_product_coupon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='categories',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(to='catalogs.Category', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='store',
            field=models.ForeignKey(to='stores.Store', null=True),
            preserve_default=True,
        ),
    ]
