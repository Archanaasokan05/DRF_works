
# --------------------------permissions-----------------------------
# # Only authenticated user can access the view
# # only organizer user can create a new event
# # only organizer of the event can perform updation/deletion
# ------------------------------------------------------------------

from rest_framework.permissions import BasePermission


class IsOrganizerOrReadOnly(BasePermission):
    def has_permission(self, request, view):    #view level
        if request.method=='GET':                             #Any logged in user (organizer/customer) can read records
            return request.user.is_authenticated
        return request.user.is_authenticated and request.user.role=='organizer' #only organizer can perform other operations

    def has_object_permission(self, request, view, obj):
        if(request.method=='GET'):
            return request.user.is_authenticated              #any logged in user can read
        return obj.organizer==request.user                    #but only organizer of the event can perform delete/update