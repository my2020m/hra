# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-14 09:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('images', '0001_initial'),
        ('wagtailcore', '0032_add_bulk_delete_page_permission'),
    ]

    operations = [
        migrations.CreateModel(
            name='CallToActionSnippet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_url', models.URLField(blank=True)),
                ('link_text', models.CharField(blank=True, max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('summary', wagtail.core.fields.RichTextField(blank=True, max_length=255)),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='images.CustomImage')),
                ('link_page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='wagtailcore.Page')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SocialMediaSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('twitter_handle', models.CharField(blank=True, help_text='Your Twitter username without the @, e.g. katyperry', max_length=255)),
                ('facebook_app_id', models.CharField(blank=True, help_text='Your Facebook app ID.', max_length=255)),
                ('default_sharing_text', models.CharField(blank=True, help_text='Default sharing text to use if social text has not been set on a page.', max_length=255)),
                ('site_name', models.CharField(blank=True, default='Health Research Authority', help_text='Site name, used by Open Graph.', max_length=255)),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
