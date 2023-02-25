from rest_framework import permissions
from rest_framework.views import Request, View

class IsAdmOrUserToUser(permissions.BasePermission):
    def has_permission(self, request: Request, view: View, ):
        if request.user.is_authenticated and request.user.is_superuser:
            return True
        if request.user.is_authenticated and request.user.id == int(view.kwargs['user_id']):
            return True
        
