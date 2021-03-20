from rest_framework import permissions


class IsEditableOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):

        return (
            obj.status != 'DELIVERED' or request.method in (
                'GET', 'HEAD', 'OPTIONS')
        )
