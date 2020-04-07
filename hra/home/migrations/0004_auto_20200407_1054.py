# Generated by Django 2.0.13 on 2020-04-07 09:54

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_new_homepage_structure'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.core.fields.StreamField([('listing', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=128, required=False)), ('display_meta_info', wagtail.core.blocks.BooleanBlock(required=False)), ('featured_pages', wagtail.core.blocks.ListBlock(wagtail.core.blocks.PageChooserBlock())), ('pages', wagtail.core.blocks.ListBlock(wagtail.core.blocks.PageChooserBlock()))])), ('highlight', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('text', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock(required=False))], template='home/blocks/highlight_block.html'))]),
        ),
    ]
