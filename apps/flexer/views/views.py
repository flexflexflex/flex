import uuid

import redis
from rest_framework.response import Response
from rest_framework.views import APIView

from ..serializers import FlexerSerializer
from core.redis_cli import cli as redis
from apps.flexer.models import Flexer
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
        code = request.POST.get('code')
        phone = request.POST.get('phone')
        generated_code = redis.get(phone)

        if code != generated_code:
            return Response({
                'error': 'code not valid'
            }, 400)

        token = generate_auth_token()

        flexer, created = Flexer.objects.get_or_create(phone=phone)
        flexer.token = token
        flexer.save()

        return Response({
            'new_user': created,
            'token': token
        }, 200)


class GetUserInfo(APIView):
    authentication_classes = [TokenAuthenticator, ]

    def get(self, request):
        return Response(FlexerSerializer(request.user).data)


def generate_auth_token():
    return str(uuid.uuid4()).replace('-', '')

