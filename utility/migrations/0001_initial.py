# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import utility.models


class Migration(migrations.Migration):

    dependencies = [
        ('basehandler', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileUpload',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data_file', models.FileField(upload_to=utility.models.user_data_file_path)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('interval', models.ForeignKey(to='basehandler.IntervalData')),
            ],
            options={
                'verbose_name': 'Upload data file',
                'verbose_name_plural': 'Upload data files',
            },
        ),
    ]
