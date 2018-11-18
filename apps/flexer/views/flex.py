from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from core.authenticators import TokenAuthenticator
from ..models import Flex
from ..serializers import FlexListSerializer, FlexDetailSerializer, FlexUserSerializer


class FlexMembersView(APIView):
    authentication_classes = [TokenAuthenticator, ]

    def get(self, request, pk):
        try:
            flex = Flex.objects.get(id=pk)
        except Flex.DoesNotExist:
            return Response({
                'error': 'Flex with id %s not found' % pk
            }, 404)

        return Response(FlexUserSerializer(flex.members, many=True, context={'request': request}).data)


class FlexView(ModelViewSet):
    authentication_classes = [TokenAuthenticator, ]
    queryset = Flex.objects.all().order_by('-created_at')
    serializer_class = FlexListSerializer

    def perform_create(self, serializer):
        serializer.save(
            owner=self.request.user
        )


class JoinFlexView(APIView):
    authentication_classes = [TokenAuthenticator, ]

    def post(self, request, pk):
        try:
            flex = Flex.objects.get(id=pk)
        except Flex.DoesNotExist:
            return Response({
                'error': 'Flex with id %s not found' % pk
            }, 404)

        flex.members.add(request.user)
        return Response(FlexDetailSerializer(flex, context={'request': request}).data)
