from rest_framework.permissions import BasePermission

class IsAuthorOrReadOnly(BasePermission):
    def  has_object_permission(self, request, view, obj):
        if request.method=="GET":   #Any user can read
            return True
        return request.user==obj.author   #only authenticated user can edit/delete