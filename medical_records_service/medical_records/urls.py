from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MedicalRecordViewSet, DiagnosisViewSet, TreatmentViewSet, MedicationViewSet, PrescriptionViewSet

router = DefaultRouter()
router.register(r'medical_records', MedicalRecordViewSet)
router.register(r'diagnoses', DiagnosisViewSet)
router.register(r'treatments', TreatmentViewSet)
router.register(r'medications', MedicationViewSet)
router.register(r'prescriptions', PrescriptionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
