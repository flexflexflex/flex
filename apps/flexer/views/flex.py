from rest_framework.generics import ListCreateAPIView

from core.authenticators import TokenAuthenticator
from ..models import Flex
from ..serializers import FlexSerializer


class FlexView(ListCreateAPIView):
    authentication_classes = [TokenAuthenticator, ]
    queryset = Flex.objects.all()
    serializer_class = FlexSerializer

    def perform_create(self, serializer):
        serializer.save(
            owner=self.request.user
        )

