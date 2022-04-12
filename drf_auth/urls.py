from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('home/', TemplateView.as_view(template_name='home.html'), name='home'),
    # path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('', include('duck.urls')),
    # path("accounts/", include("accounts.urls")),
    # path('accounts/', include('django.contrib.auth.urls')),
]
