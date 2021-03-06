# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-10 16:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='exercises.Person')),
                ('salary', models.DecimalField(decimal_places=2, default=0.0, max_digits=7)),
                ('position_name', models.CharField(max_length=64)),
            ],
        ),
    ]
