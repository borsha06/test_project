# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-18 04:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('institute', '0001_initial'),
        ('district', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('std_id', models.IntegerField(primary_key=True, serialize=False)),
                ('std_name', models.CharField(max_length=200)),
                ('std_phone', models.CharField(max_length=15)),
                ('std_admission', models.DateField()),
                ('dist_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='district.District')),
                ('ins_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institute.Institute')),
            ],
        ),
    ]