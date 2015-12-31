# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('utility', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fileupload',
            name='status',
            field=models.CharField(default=b'To be Upload', max_length=15),
        ),
    ]
