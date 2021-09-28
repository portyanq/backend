from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView, TokenVerifyView)

from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    # path('token/login/', include('djoser.urls.jwt')),
    # path('token/logout/', include('djoser.urls.jwt')),

    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh', TokenRefreshView.as_view()),
    path('api/token/verify', TokenVerifyView.as_view()),

    path('api/v1/', include('app.urls')),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)