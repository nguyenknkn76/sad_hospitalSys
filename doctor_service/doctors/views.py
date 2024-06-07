from rest_framework import viewsets
from .models import Doctor, DoctorLicense, Specialty
from .serializers import DoctorSerializer, DoctorLicenseSerializer, SpecialtySerializer

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class DoctorLicenseViewSet(viewsets.ModelViewSet):
    queryset = DoctorLicense.objects.all()
    serializer_class = DoctorLicenseSerializer

class SpecialtyViewSet(viewsets.ModelViewSet):
    queryset = Specialty.objects.all()
    serializer_class = SpecialtySerializer
