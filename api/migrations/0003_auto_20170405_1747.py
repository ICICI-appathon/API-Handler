# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20170329_1905'),
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
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='financialgoal',
            name='CustomerID',
            field=models.ForeignKey(default=datetime.date(2017, 4, 5), to='api.Customer'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transaction',
            name='Location',
            field=models.CharField(default=b'NULL', max_length=250),
            preserve_default=True,
        ),
    ]
