from rest_framework import permissions

class OwnerAuthenticated(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        return super().has_object_permission(request, view, obj) and request.user == obj.user


class IsDoctor(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.user_type == 'doctor'

class IsNurse(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.user_type == 'nurse'

class IsPatient(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.user_type == 'patient'
