from rest_framework import serializers
from shops.models import Shop


class ShopSerializer(serializers.ModelSerializer):

    def update(self, instance, validated_data):
        if validated_data.__getitem__('connected_users'):
            for i in instance.connected_users.all():
                if i.id == validated_data['connected_users'][0].id:
                    instance.connected_users.remove(validated_data['connected_users'][0].id)
                    break
            else:
                instance.connected_users.add(validated_data['connected_users'][0].id)
        return instance

    class Meta:
        model = Shop
        fields = '__all__'


class ShopListCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Shop
        fields = '__all__'
