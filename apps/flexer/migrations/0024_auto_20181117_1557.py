# Generated by Django 2.1 on 2018-11-17 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flexer', '0023_auto_20181117_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flex',
            name='description',
            field=models.CharField(blank=True, default='', max_length=300),
        ),
    ]
