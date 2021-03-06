# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-28 20:53
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('frontdesk', '0004_auto_20160923_1511'),
    ]

    operations = [
        migrations.CreateModel(
            name='XMLMemberControlAttrs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sps_check_status', model_utils.fields.StatusField(choices=[('valid', 'valid'), ('invalid', 'invalid')], default='valid', max_length=100, no_check_for_status=True)),
                ('sps_check_status_changed', model_utils.fields.MonitorField(default=django.utils.timezone.now, monitor='sps_check_status')),
                ('sps_check_details', django.contrib.postgres.fields.jsonb.JSONField()),
                ('member', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='xml_control_attrs', to='frontdesk.PackageMember')),
            ],
        ),
    ]
