from django.urls import path, include

from apps.flexer.views import (GenerateCode,
                               GenerateToken,
                               UserReadUpdateView,
                               FriendsViewSet,
                               FlexView,
                               CheckUsernameView,
                               JoinFlexView)

app_name = 'v1'

auth_urls = [
    path('code/', GenerateCode.as_view(), name='code'),
    path('token/', GenerateToken.as_view(), name='token'),
    path('check/<str:username>/', CheckUsernameView.as_view(), name='check-username'),
]

flex_urls = [
    path('<int:pk>/join/', JoinFlexView.as_view(), name='join'),
    path('<int:pk>/', FlexView.as_view({'get': 'retrieve', 'patch': 'update'}), name='details-update'),
    path('', FlexView.as_view({'get': 'list', 'post': 'create'}), name='list-create'),
]

user_urls = [
    path('', UserReadUpdateView.as_view(), name='user'),
    path('friends/', FriendsViewSet.as_view({'get': 'list'}), name='user-friends'),
]

urlpatterns = [
    path('auth/', include((auth_urls, 'auth'), namespace='auth')),
    path('user/', include((user_urls, 'user'), namespace='user')),
    path('flex/', include((flex_urls, 'flex'), namespace='flex'))
]
