from rest_framework.viewsets import ModelViewSet

from core.authenticators import TokenAuthenticator
from ..models import Flex
from ..serializers import FlexSerializer


class FlexView(ModelViewSet):
    authentication_classes = [TokenAuthenticator, ]
    queryset = Flex.objects.all().order_by('-created_at')
    serializer_class = FlexSerializer

    def perform_create(self, serializer):
        serializer.save(
            owner=self.request.user
        )

