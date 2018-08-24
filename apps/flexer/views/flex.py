from rest_framework.generics import ListAPIView

from core.authenticators import TokenAuthenticator
from ..models import Flex
from ..serializers import FlexSerializer


class FlexListView(ListAPIView):
    authentication_classes = [TokenAuthenticator, ]
    queryset = Flex.objects.all()
    serializer_class = FlexSerializer

