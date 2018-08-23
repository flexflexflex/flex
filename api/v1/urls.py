from django.urls import path, include

from apps.flexer.views import GenerateCode, GenerateToken, GetUserInfo

app_name = 'v1'

auth_urls = [
    path('code/', GenerateCode.as_view(), name='code'),
    path('token/', GenerateToken.as_view(), name='token'),
    path('info/', GetUserInfo.as_view(), name='token'),
]

urlpatterns = [
    path('auth/', include((auth_urls, 'auth'), namespace='auth'))
]
