# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_transaction_ammount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='Ammount',
            field=models.IntegerField(default=0, max_length=250),
        ),
    ]
