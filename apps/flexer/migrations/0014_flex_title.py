# Generated by Django 2.1 on 2018-08-26 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flexer', '0013_auto_20180826_0901'),
    ]

    operations = [
        migrations.AddField(
            model_name='flex',
            name='title',
            field=models.CharField(default='', max_length=200),
        ),
    ]
