# Generated by Django 2.1 on 2018-09-25 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flexer', '0018_auto_20180901_1706'),
    ]

    operations = [
        migrations.AddField(
            model_name='flex',
            name='photo',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]