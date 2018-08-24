import uuid

import redis
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateAPIView

from ..serializers import FlexUserSerializer
from core.redis_cli import cli as redis
from apps.flexer.models import FlexUser
from core.authenticators import TokenAuthenticator


class GenerateCode(APIView):

    def post(self, request):
        phone = request.POST.get('phone')
        # code = str(randint(1000, 9999))
        code = '0000'
        redis.set(phone, code)

        return Response({
            'result': 'ok'
        }, status=200)


class GenerateToken(APIView):
    def post(self, request):
        code = request.data.get('code')
        phone = request.data.get('phone')
        generated_code = redis.get(phone)

        if code != generated_code:
            return Response({
                'error': 'code not valid'
            }, 400)

        token = generate_auth_token()

        flexer, created = FlexUser.objects.get_or_create(phone=phone)
        flexer.token = token
        flexer.save()

        return Response({
            'new_user': created,
            'token': token
        }, 200)


class UserReadUpdateView(RetrieveUpdateAPIView):
    authentication_classes = [TokenAuthenticator, ]
    serializer_class = FlexUserSerializer

    def get_object(self):
        return self.request.user


class SubscribeView(APIView):
    authentication_classes = [TokenAuthenticator, ]

    def post(self, request):
        to = request.POST.get('to')

        if not to:
            raise ValidationError({
                'error': 'user is not provided'
            })

        follow_to = FlexUser.objects.get(username=to)

        request.user.subscribed.add(follow_to)


def generate_auth_token():
    return str(uuid.uuid4()).replace('-', '')

