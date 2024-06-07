from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DoctorViewSet, DoctorLicenseViewSet, SpecialtyViewSet

router = DefaultRouter()
router.register(r'doctors', DoctorViewSet)
router.register(r'doctor-licenses', DoctorLicenseViewSet)
router.register(r'specialties', SpecialtyViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
