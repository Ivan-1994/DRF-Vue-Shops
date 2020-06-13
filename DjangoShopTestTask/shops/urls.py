from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from shops.views import ShopListViewSet, ShopViewSet

shop_list = ShopListViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

shop_detail = ShopViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})


urlpatterns = format_suffix_patterns([
    path('shops/', shop_list, name='shop-list'),
    path('shop/<int:shop_id>', shop_detail, name='shop-detail'),
])
