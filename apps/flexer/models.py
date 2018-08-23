from django.db import models


class Flexer(models.Model):
    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, default='')
    bio = models.CharField(max_length=200, default='')

    phone = models.CharField(max_length=12)
    username = models.CharField(max_length=10, default='')

    token = models.CharField(max_length=32, default='')


