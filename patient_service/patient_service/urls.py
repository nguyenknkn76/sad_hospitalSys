from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('patients.urls')),  # Đảm bảo rằng dòng này có trong file urls.py của project chính
]
