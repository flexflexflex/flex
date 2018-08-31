from rest_framework.test import APITestCase


class AuthorizedTestCase(APITestCase):
    def __init__(self, methodName='runTest'):
        super().__init__(methodName)
        self.client.credentials(HTTP_AUTHORIZATION='123123123123')



