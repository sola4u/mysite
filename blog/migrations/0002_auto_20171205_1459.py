# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-05 14:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='tags',
            new_name='tag',
        ),
    ]