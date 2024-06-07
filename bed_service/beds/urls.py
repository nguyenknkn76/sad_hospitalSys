from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClinicViewSet, BedViewSet

router = DefaultRouter()
router.register(r'clinics', ClinicViewSet)
router.register(r'beds', BedViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
