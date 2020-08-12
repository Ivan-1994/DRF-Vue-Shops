from rest_framework import permissions


class IsOwnerProfileOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if str(request.user) == 'AnonymousUser':
            return False
        return obj.id == request.user.id or request.user.user_type == '2'


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action == 'create':
            return True
        if str(request.user) == 'AnonymousUser':
            return False
        return request.user.user_type == '2'
