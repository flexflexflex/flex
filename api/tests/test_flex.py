from django.urls import reverse
from .base import AuthorizedTestCase


class FlexTestCase(AuthorizedTestCase):
    def setUp(self):
        self.list_url = reverse('api:v1:flex:list-create')
        # self.client.credentials(HTTP_AUTHORIZATION='123123123123')

    def test_can_get_flex_list(self):
        response = self.client.get(self.list_url)

        assert False, response.data


