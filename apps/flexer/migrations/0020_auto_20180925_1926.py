# Generated by Django 2.1 on 2018-09-25 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flexer', '0019_flex_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flex',
            old_name='photo',
            new_name='image',
        ),
    ]
