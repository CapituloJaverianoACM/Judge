from rest_framework import permissions
from .service import UserService


class AdminPermissions(permissions.BasePermission):

    def has_permission(self, request, view):

        if not request.user.is_authenticated:
            return False
        profile = request.user.profile
        if profile.rol != 0:
            return False
        return True
