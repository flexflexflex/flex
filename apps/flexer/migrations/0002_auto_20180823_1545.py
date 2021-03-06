# Generated by Django 2.1 on 2018-08-23 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flexer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flexer',
            name='bio',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='flexer',
            name='username',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='flexer',
            name='first_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='flexer',
            name='last_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='flexer',
            name='phone',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='flexer',
            name='token',
            field=models.CharField(default='', max_length=32),
        ),
    ]
