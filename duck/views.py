from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import generics, authentication, permissions
from .serializer import DuckSerializer, UserSerializer
from .models import DuckModel
from .permissions import IsOwner
# from django.core.exceptions import PermissionDenied
# from django.shortcuts import get_object_or_404


class HelloView(APIView):
    permission_classes = (IsOwner,)

    def get(self, request):
      content = {'message': 'Hello, World!'}
      return Response(content)


class DuckList(generics.ListCreateAPIView):
  permission_classes = (IsAuthenticated,)
  # authentication_classes = [authentication.TokenAuthentication]
  queryset = DuckModel.objects.all()
  serializer_class = DuckSerializer

  def perform_create(self, serializer):
    serializer.save(owner=self.request.user)


class DuckDetail(generics.RetrieveUpdateDestroyAPIView):
  premission_classes = (IsOwner,)
  # authentication_classes = [authentication.TokenAuthentication]
  queryset = DuckModel.objects.all()
  serializer_class = DuckSerializer


# class DuckDetail(APIView):
#   premission_classes = (IsOwner,)
#   queryset = DuckModel.objects.all()
#   serializer_class = DuckSerializer

#   def get(self):
#     def get_object(self):
#       obj = get_object_or_404(self.get_queryset(), pk)
#       self.check_object_permissions(self.request, obj)
#       return obj
    
#     obj = get_object()
#     return Response(obj)
