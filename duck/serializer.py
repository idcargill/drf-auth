from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from duck.models import DuckModel


class DuckSerializer(serializers.ModelSerializer):
  owner = serializers.ReadOnlyField(source='owner.username')
  # blogger = serializers.PrimaryKeyRelatedField(many=True, queryset=DuckModel.objects.all())
  class Meta:
    fields    = ('owner', 'title', 'details', 'create_date')
    model     = DuckModel



class UserSerializer(serializers.ModelSerializer):
  username = serializers.PrimaryKeyRelatedField(many=True, queryset=DuckModel.objects.all())

  class Meta:
    model   = DuckModel
    fields  = ['username']