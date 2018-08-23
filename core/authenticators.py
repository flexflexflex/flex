from rest_framework import authentication, exceptions
from apps.flexer.models import Flexer


class TokenAuthenticator(authentication.BaseAuthentication):
    def authenticate(self, request):
        token = request.META.get('HTTP_AUTHORIZATION')

        if not token:
            raise exceptions.AuthenticationFailed('No token')

        try:
            user = Flexer.objects.get(token=token)
        except Flexer.DoesNotExist:
            raise exceptions.AuthenticationFailed('Token is invalid or expired')

        return (user, None)