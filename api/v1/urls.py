from django.urls import path, include

from apps.flexer.views import GenerateCode, GenerateToken, UserReadUpdateView, FlexView

app_name = 'v1'

auth_urls = [
    path('code/', GenerateCode.as_view(), name='code'),
    path('token/', GenerateToken.as_view(), name='token'),
    path('user/', UserReadUpdateView.as_view(), name='user'),
]

flex_urls = [
    path('', FlexView.as_view(), name='list')
]

urlpatterns = [
    path('auth/', include((auth_urls, 'auth'), namespace='auth')),
    path('flex/', include((flex_urls, 'flex'), namespace='flex'))
]
