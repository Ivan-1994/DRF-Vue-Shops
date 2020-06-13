from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shops.urls')),
    path('', include('users.urls')),
    path('auth/', include('djoser.urls'), name='auth-rest'),
    path('auth/', include('djoser.urls.authtoken'), name='auth-rest-token'),
    path('base-auth', include('rest_framework.urls')),
]
