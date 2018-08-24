from django.db import models


class FlexUser(models.Model):
    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, default='')
    bio = models.CharField(max_length=200, default='')

    phone = models.CharField(max_length=12)
    username = models.CharField(max_length=10, default='', unique=True)

    token = models.CharField(max_length=32, default='', unique=True)
    followed = models.ManyToManyField(to='FlexUser', blank=True)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username


class Flex(models.Model):
    owner = models.ForeignKey(to='FlexUser', on_delete=models.CASCADE)
    members = models.ManyToManyField(to='FlexUser', related_name='members')

    description = models.TextField()

    class Meta:
        verbose_name = 'Flex'
        verbose_name_plural = 'Flexes'

    def __str__(self):
        return '%s : %s' % ('Flex', self.owner.username)

    def get_members_count(self):
        return self.members.count()

