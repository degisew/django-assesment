from rest_framework import permissions


class IsAdmin(permissions.BasePermission):
    """
    Custom permission to allow only admins to access a view.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'admin'


class IsCoach(permissions.BasePermission):
    """
    Custom permission to allow only coaches to access a view.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'coach'


class IsAgent(permissions.BasePermission):
    """
    Custom permission to allow only agents to access a view.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'agent'


class IsFootballPlayer(permissions.BasePermission):
    """
    Custom permission to allow only football players to access a view.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'football_player'
