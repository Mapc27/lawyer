from rest_framework.permissions import BasePermission, IsAuthenticated, AllowAny


class CustomAuthPermission(BasePermission):
    def has_permission(self, request, view):
        if view.action in ('create',):
            return AllowAny
        if view.action in ('retrieve', 'list'):
            return IsAuthenticated().has_permission(request, view)
