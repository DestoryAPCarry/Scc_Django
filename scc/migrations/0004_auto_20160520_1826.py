# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-20 10:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scc', '0003_auto_20160519_0917'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skill_admin',
            old_name='emial',
            new_name='email',
        ),
    ]