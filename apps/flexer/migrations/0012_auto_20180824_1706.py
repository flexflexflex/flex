# Generated by Django 2.1 on 2018-08-24 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flexer', '0011_auto_20180824_1702'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flexuser',
            old_name='subscribed',
            new_name='followed',
        ),
    ]
