# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basehandler', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyStatsFigure',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.DecimalField(max_digits=5, decimal_places=2)),
                ('company', models.ForeignKey(to='basehandler.Company')),
                ('month', models.ForeignKey(to='basehandler.IntervalData')),
                ('param', models.ForeignKey(to='basehandler.Parameter')),
            ],
        ),
    ]
