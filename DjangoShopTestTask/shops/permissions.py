from rest_framework import permissions


class IsOwnerShopOrAdminOrRetrieve(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if view.action == 'retrieve':
            return True
        if str(request.user) == 'AnonymousUser':
            return False
        return obj.user.id == request.user.id or request.user.user_type == '2'


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if str(request.user) == 'AnonymousUser':
            return False
        return request.user.user_type == '2'
