# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField(null=True, blank=True)),
                ('slug', models.SlugField(unique=True)),
                ('logo', models.ImageField(upload_to=b'stores/logos')),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StoreCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField()),
                ('category', models.ManyToManyField(to='catalogs.Category')),
                ('store', models.ForeignKey(to='stores.Store')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StoreProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address1', models.CharField(max_length=120)),
                ('address2', models.CharField(max_length=120)),
                ('city', models.CharField(max_length=120)),
                ('country', models.CharField(max_length=120)),
                ('zipcode', models.CharField(max_length=120)),
                ('mobile', models.CharField(max_length=12)),
                ('telephone', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=75)),
                ('website', models.URLField()),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('store', models.ForeignKey(to='stores.Store')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='store',
            unique_together=set([('title', 'slug')]),
        ),
    ]
