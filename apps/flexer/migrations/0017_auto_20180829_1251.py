# Generated by Django 2.1 on 2018-08-29 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flexer', '0016_auto_20180829_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flex',
            name='description',
            field=models.CharField(blank=True, default='', max_length=120),
        ),
        migrations.AlterField(
            model_name='flex',
            name='members',
            field=models.ManyToManyField(blank=True, related_name='members', to='flexer.FlexUser'),
        ),
    ]
