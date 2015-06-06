# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('organization_name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=20)),
                ('contact_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=200)),
            ],
        ),
    ]
