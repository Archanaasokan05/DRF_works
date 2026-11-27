# from rest_framework.permissions import BasePermission
#
# class IsOwner(BasePermission):
#     def  has_object_permission(self, request, view, obj):
#         # return obj.user
#         if request.method=="GET":   #Any user can read
#             return True
#         return request.user==obj.user   #only creator of the object can update/delete
#
# # condition obj.user==request.user checks whether the creator of the object and requested user are same
#

from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user==request.user