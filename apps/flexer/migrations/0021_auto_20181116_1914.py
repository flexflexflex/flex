# Generated by Django 2.1 on 2018-11-16 19:14

from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('flexer', '0020_auto_20180925_1926'),
    ]

    operations = [
        migrations.AddField(
            model_name='flex',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='flex',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='flex',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(upload_to=''),
        ),
    ]
