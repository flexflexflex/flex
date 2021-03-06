from django.db import models, transaction
from django.utils import timezone
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit

from core.fcm import send_push


class FlexUser(models.Model):
    photo = ProcessedImageField(processors=[ResizeToFit(width=800, upscale=False)],
                                blank=True,
                                null=True)

    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, default='')
    bio = models.CharField(max_length=200, default='')

    phone = models.CharField(max_length=12)
    username = models.CharField(max_length=10, null=True, unique=True)

    token = models.CharField(max_length=32, default='', unique=True)
    friends = models.ManyToManyField(to='FlexUser', blank=True)

    fcm_registration_id = models.CharField(max_length=200, blank=True, null=True)

    def add_friend(self, user):
        with transaction.atomic():
            self.friends.add(user)
            user.friends.add(self)

    def send_push(self, title, text, extra):
        send_push(
            self.fcm_registration_id,
            title,
            text,
            extra
        )

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username or '-'


class Flex(models.Model):
    owner = models.ForeignKey(to='FlexUser', on_delete=models.CASCADE)
    members = models.ManyToManyField(to='FlexUser', related_name='members', blank=True)

    title = models.CharField(max_length=200)
    description = models.CharField(default='', blank=True, max_length=300)

    image = ProcessedImageField(processors=[ResizeToFit(width=500, upscale=False)])

    created_at = models.DateTimeField(default=timezone.now)

    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    class Meta:
        verbose_name = 'Flex'
        verbose_name_plural = 'Flexes'

    def __str__(self):
        return '%s : %s' % ('Flex', self.owner.username or '-')

    def get_members_count(self):
        return self.members.count()

