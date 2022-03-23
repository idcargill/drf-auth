from django.urls import path
from .views import HelloView
from .views import DuckList, DuckDetail

urlpatterns = [
    path('hello/', HelloView.as_view(), name='hello'),
    path('', DuckList.as_view(), name='duck_list'),
    path('<int:pk>/', DuckDetail.as_view(), name='duck_detail'),
]