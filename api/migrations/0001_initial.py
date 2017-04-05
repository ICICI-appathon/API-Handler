# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('accountNumber', models.CharField(default=b'NULL', max_length=250)),
                ('Branch', models.CharField(default=b'NULL', max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cardNumber', models.CharField(default=b'NULL', max_length=250)),
                ('Limit', models.CharField(default=b'NULL', max_length=250)),
                ('Type', models.CharField(default=b'NULL', max_length=250)),
                ('Account', models.ForeignKey(blank=True, to='api.Account', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='cashWallet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Balance', models.IntegerField(default=0, max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
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
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('CustomerID', models.CharField(default=b'NULL', max_length=250)),
                ('Name', models.CharField(default=b'NULL', max_length=250)),
                ('Address', models.CharField(default=b'NULL', max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='financialGoal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Ammount', models.CharField(default=b'NULL', max_length=250)),
                ('timeFrame', models.CharField(default=b'NULL', max_length=250)),
                ('CustomerID', models.ForeignKey(to='api.Customer')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='forexTransactions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Ammount', models.IntegerField(default=0, max_length=250)),
                ('Currency', models.ForeignKey(to='api.Currency')),
                ('CustomerID', models.ForeignKey(to='api.Customer')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='forexWallet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Balance', models.IntegerField(default=0, max_length=250)),
                ('Currency', models.ForeignKey(to='api.Currency')),
                ('CustomerID', models.ForeignKey(to='api.Customer')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='loansPolicies',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('loanID', models.CharField(default=b'NULL', max_length=250)),
                ('Installment', models.CharField(default=b'NULL', max_length=250)),
                ('CustomerID', models.ForeignKey(to='api.Customer')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Location', models.CharField(default=b'NULL', max_length=250)),
                ('TransactionID', models.CharField(default=b'NULL', max_length=250)),
                ('Date', models.CharField(default=b'NULL', max_length=250)),
                ('Time', models.CharField(default=b'NULL', max_length=250)),
                ('Account', models.ForeignKey(blank=True, to='api.Account', null=True)),
                ('Card', models.ForeignKey(blank=True, to='api.Card', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='transactionCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Category', models.CharField(default=b'NULL', max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='transactionMode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Mode', models.CharField(default=b'Cash', max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='transactionType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Type', models.CharField(default=b'Credit', max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='transaction',
            name='Category',
            field=models.ForeignKey(to='api.transactionCategory'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='transaction',
            name='CustomerID',
            field=models.ForeignKey(to='api.Customer'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='transaction',
            name='Mode',
            field=models.ForeignKey(to='api.transactionMode'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='transaction',
            name='Type',
            field=models.ForeignKey(to='api.transactionType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cashwallet',
            name='CustomerID',
            field=models.ForeignKey(to='api.Customer'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='account',
            name='CustomerID',
            field=models.ForeignKey(to='api.Customer'),
            preserve_default=True,
        ),
    ]
