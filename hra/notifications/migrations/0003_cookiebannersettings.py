# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-03-04 14:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0039_collectionviewrestriction'),
        ('notifications', '0002_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CookieBannerSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=False, verbose_name='Active')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('text', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('policy_page', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wagtailcore.Page')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
