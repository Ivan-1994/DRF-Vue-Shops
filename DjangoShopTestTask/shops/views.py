from rest_framework import viewsets, mixins

from shops.models import Shop
from shops.serializers import ShopSerializer, ShopListCreateSerializer
from shops.permissions import IsOwnerShopOrAdminOrRetrieve


class ShopListViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopListCreateSerializer


class ShopViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    permission_classes = [IsOwnerShopOrAdminOrRetrieve]
    lookup_field = 'shop_id'
