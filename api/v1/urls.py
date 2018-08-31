from django.urls import path, include

from apps.flexer.views import GenerateCode, GenerateToken, UserReadUpdateView, FlexView, CheckUsernameView

app_name = 'v1'

auth_urls = [
    path('code/', GenerateCode.as_view(), name='code'),
    path('token/', GenerateToken.as_view(), name='token'),
    path('user/', UserReadUpdateView.as_view(), name='user'),
    path('check/<str:username>/', CheckUsernameView.as_view(), name='check-username'),
]

flex_urls = [
    path('<int:pk>/', FlexView.as_view({'get': 'retrieve', 'patch': 'update'}), name='details-update'),
    path('', FlexView.as_view({'get': 'list', 'post': 'create'}), name='list-create'),
]

urlpatterns = [
    path('auth/', include((auth_urls, 'auth'), namespace='auth')),
    path('flex/', include((flex_urls, 'flex'), namespace='flex'))
]
