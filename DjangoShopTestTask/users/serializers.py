from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=False)

    def to_representation(self, value):
        return {
            "id": value.id,
            "last_login": value.last_login,
            "email": value.email,
            "first_name": value.first_name,
            "last_name": value.last_name,
            "user_type": value.user_type
        }

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        user = super().update(instance, validated_data)
        try:
            user.set_password(validated_data['password'])
            user.save()
        except KeyError:
            pass
        return user
