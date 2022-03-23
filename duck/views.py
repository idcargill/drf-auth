from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import generics
from .serializer import DuckSerializer
from .models import DuckModel

class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)

class DuckList(generics.ListCreateAPIView):
  permission_classes = (IsAuthenticated, )
  queryset = DuckModel.objects.all()
  serializer_class = DuckSerializer

class DuckDetail(generics.RetrieveUpdateDestroyAPIView):
  premission_classes = (IsAuthenticated,)
  queryset = DuckModel.objects.all()
  serializer_class = DuckSerializer

