from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from users.views import UserListViewSet, UserViewSet, activate_user

user_list = UserListViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

user_detail = UserViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

urlpatterns = format_suffix_patterns([
    path('users/', user_list, name='user-list'),
    path('user/<int:id>', user_detail, name='user-detail'),
    path('activate_email/<int:id>/<str:activate>', activate_user, name='user-activate'),
])
