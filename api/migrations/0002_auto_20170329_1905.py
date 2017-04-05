# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Currency', models.CharField(default=b'NULL', max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='card',
            name='Account',
            field=models.ForeignKey(blank=True, to='api.Account', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cashwallet',
            name='Balance',
            field=models.IntegerField(default=0, max_length=250),
        ),
        migrations.AlterField(
            model_name='financialgoal',
            name='timeFrame',
            field=models.CharField(default=b'NULL', max_length=250),
        ),
        migrations.AlterField(
            model_name='forextransactions',
            name='Ammount',
            field=models.IntegerField(default=0, max_length=250),
        ),
        migrations.AlterField(
            model_name='forextransactions',
            name='Currency',
            field=models.ForeignKey(to='api.Currency'),
        ),
        migrations.AlterField(
            model_name='forexwallet',
            name='Balance',
            field=models.IntegerField(default=0, max_length=250),
        ),
        migrations.AlterField(
            model_name='forexwallet',
            name='Currency',
            field=models.ForeignKey(to='api.Currency'),
        ),
    ]
