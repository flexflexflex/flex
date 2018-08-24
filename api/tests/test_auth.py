from django.test import TestCase
from django.urls import reverse

from apps.flexer.models import FlexUser
from core.redis_cli import cli as redis


class RegisterTestCase(TestCase):
    def setUp(self):
        self.phone = '998909999999'
        self.token_url = reverse('api:v1:auth:token')
        self.code_url = reverse('api:v1:auth:code')

    def test_can_generate_auth_code(self):

        self.client.post(self.code_url, {
            'phone': self.phone
        })

        code = redis.get(self.phone)
        assert code == '0000', code

    def test_can_get_token(self):

        self.client.post(self.code_url, {
            'phone': self.phone
        })

        code = redis.get(self.phone)
        data = {
            'phone': self.phone,
            'code': code
        }

        response = self.client.post(self.token_url, data)

        token = response.json().get('token')
        flex_user = FlexUser.objects.get(phone=self.phone)

        assert token == flex_user.token, '%s %s' % (token, flex_user.token)
