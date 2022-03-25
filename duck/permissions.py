from rest_framework import permissions


class IsOwner(permissions.BasePermission):
  def has_permission(self, request, view):
    return request.user.is_user


  def has_object_permission(self, request, view, obj):
    if request.method in permissions.SAFE_METHODS:
      return True

    if obj.owner is None:
      return False
  
    return  obj.owner == request.user
