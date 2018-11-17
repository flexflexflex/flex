from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from apps.flexer.serializers import FlexUserSerializer
from core.authenticators import TokenAuthenticator


class UserReadUpdateView(RetrieveUpdateAPIView):
    authentication_classes = [TokenAuthenticator, ]
    serializer_class = FlexUserSerializer

    def get_object(self):
        return self.request.user


class FriendsViewSet(GenericViewSet):
    authentication_classes = [TokenAuthenticator, ]
    serializer_class = FlexUserSerializer

    def list(self, request):
        friends = self.request.user.friends.all()

        page = self.paginate_queryset(friends)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.serializer_class(friends, many=True)
        return Response(serializer.data)

    def post(self):
        pass

    def delete(self):
        pass
