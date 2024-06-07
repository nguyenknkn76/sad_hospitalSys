import requests
from rest_framework import viewsets
from .models import Clinic, Bed
from .serializers import ClinicSerializer, BedSerializer

class ClinicViewSet(viewsets.ModelViewSet):
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer

class BedViewSet(viewsets.ModelViewSet):
    queryset = Bed.objects.all()
    serializer_class = BedSerializer

    def retrieve_patient(self, patient_id):
        response = requests.get(f'http://127.0.0.1:8002/api/patients/{patient_id}/')
        if response.status_code == 200:
            return response.json()
        return None
