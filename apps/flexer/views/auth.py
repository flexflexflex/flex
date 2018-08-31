import redisfrom rest_framework.exceptions import ValidationErrorfrom rest_framework.generics import RetrieveUpdateAPIViewfrom rest_framework.response import Responsefrom rest_framework.views import APIViewfrom apps.flexer.models import FlexUserfrom core.authenticators import TokenAuthenticatorfrom core.redis_cli import cli as redisfrom core.utils import generate_auth_tokenfrom ..serializers import FlexUserSerializer, GenerateTokenSerializer, GenerateCodeSerializerclass GenerateCode(APIView):    def post(self, request):        serializer = GenerateCodeSerializer(data=request.data)        if not serializer.is_valid():            return Response({                'errors': serializer.errors            }, 400)        phone = serializer.validated_data['phone']        # code = str(randint(1000, 9999))        code = '0000'        redis.set(phone, code)        return Response({            'result': 'ok'        }, status=200)class GenerateToken(APIView):    def post(self, request):        serializer = GenerateTokenSerializer(data=request.data)        if not serializer.is_valid():            return Response({                'errors': serializer.errors,            }, 400)        phone = serializer.validated_data['phone']        code = serializer.validated_data['code']        generated_code = redis.get(phone)        if code != generated_code:            return Response({                'error': 'code not valid'            }, 400)        token = generate_auth_token()        flexer, created = FlexUser.objects.get_or_create(phone=phone)        flexer.token = token        flexer.save()        return Response({            'new_user': created,            'token': token        }, 200)class UserReadUpdateView(RetrieveUpdateAPIView):    authentication_classes = [TokenAuthenticator, ]    serializer_class = FlexUserSerializer    def get_object(self):        return self.request.userclass CheckUsernameView(APIView):    authentication_classes = [TokenAuthenticator, ]    def get(self, request, username):        return Response({            'valid': not FlexUser.objects.filter(username=username).exists()        })class SubscribeView(APIView):    authentication_classes = [TokenAuthenticator, ]    def post(self, request):        to = request.POST.get('to')        if not to:            raise ValidationError({                'error': 'user is not provided'            })        follow_to = FlexUser.objects.get(username=to)        request.user.subscribed.add(follow_to)        return Response({            'result': 'ok'        })