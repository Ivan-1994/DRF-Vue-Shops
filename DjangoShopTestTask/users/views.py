from rest_framework import viewsets, mixins, permissions
from django.http import HttpResponse
from users.models import User
from users.serializers import UserSerializer
from users.permissions import IsAdmin, IsOwnerProfileOrAdmin


def activate_user(request, id, activate):
    try:
        user = User.objects.get(pk=id)
        if user.uuid == activate:
            user.is_active = True
            user.save()
        return HttpResponse(status=200)
    except:
        return HttpResponse(status=404)


class UserListViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdmin]


class UserViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsOwnerProfileOrAdmin]
    lookup_field = 'id'
