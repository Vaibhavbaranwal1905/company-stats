# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('singleview', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='companystatsfigure',
            old_name='month',
            new_name='interval',
        ),
    ]
