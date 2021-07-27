from rest_framework.permissions import BasePermission

from . import models


class IsManager(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == models.UserRole.MANAGER
