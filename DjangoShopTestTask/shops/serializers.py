from rest_framework import serializers

from shops.models import Shop


class ShopSerializer(serializers.ModelSerializer):
    user = serializers.IntegerField(source='user.id')

    # def update(self, instance, validated_data):
    #     print(validated_data)
    #     shop = super().update(instance, validated_data)
    #     try:
    #         for i in validated_data['connected_users']:
    #             shop.connected_users.remove(i.id)
    #         shop.save()
    #     except KeyError:
    #         pass
    #     return shop

    class Meta:
        model = Shop
        fields = '__all__'
