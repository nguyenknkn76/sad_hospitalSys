from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientViewSet, AddressViewSet, InsuranceViewSet

router = DefaultRouter()
router.register(r'patients', PatientViewSet)
router.register(r'addresses', AddressViewSet)
router.register(r'insurances', InsuranceViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Đảm bảo rằng bạn đã định nghĩa đường dẫn gốc
]
