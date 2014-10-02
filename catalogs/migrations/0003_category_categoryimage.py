# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogs', '0002_category_stores'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='categoryimage',
            field=models.ImageField(null=True, upload_to=b'categories/images', blank=True),
            preserve_default=True,
        ),
    ]
