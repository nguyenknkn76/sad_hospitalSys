from django.contrib import admin
from django.urls import path, include
from .views import auth_service_proxy

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', auth_service_proxy),
    # path('api/auth/', include('auth.urls')), 
]
