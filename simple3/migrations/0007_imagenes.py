# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-21 22:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simple3', '0006_compresores'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imagenes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=10000, null=True)),
            ],
        ),
    ]
