from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from duck.models import DuckModel


class DuckSerializer(serializers.ModelSerializer):
  class Meta:
    fields    = ('owner', 'title', 'details', 'create_date')
    model     = DuckModel