# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='loansPolicies',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ID', models.CharField(default=b'NULL', max_length=250)),
                ('Installment', models.CharField(default=b'NULL', max_length=250)),
                ('CustomerID', models.ForeignKey(to='api.Customer')),
            ],
        ),
        migrations.AddField(
            model_name='financialgoal',
            name='CustomerID',
            field=models.ForeignKey(default=datetime.datetime(2017, 3, 29, 21, 1, 13, 988547, tzinfo=utc), to='api.Customer'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transaction',
            name='Location',
            field=models.CharField(default=b'NULL', max_length=250),
        ),
    ]
