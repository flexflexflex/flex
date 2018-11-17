from rest_framework import authentication, exceptions
from apps.flexer.models import FlexUser


class TokenAuthenticator(authentication.BaseAuthentication):
    def authenticate(self, request):
        token = request.META.get('HTTP_AUTHORIZATION')

        if not token:
            raise exceptions.AuthenticationFailed('Token is not provided')

        token = token.replace('Token ', '')

        try:
            user = FlexUser.objects.get(token=token)
        except FlexUser.DoesNotExist:
            raise exceptions.AuthenticationFailed('Token is invalid or expired. Your token: %s' % token)

        return user, None

