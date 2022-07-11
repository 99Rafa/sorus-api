from rest_framework import permissions


class IsAdmin(permissions.BasePermission):
    message = 'You are not an admin user'

    def has_permission(self, request, view):
        return request.user.user_type.id == 1