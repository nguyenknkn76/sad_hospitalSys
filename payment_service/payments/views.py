import requests
from rest_framework import viewsets
from .models import Bill, Payment
from .serializers import BillSerializer, PaymentSerializer

class BillViewSet(viewsets.ModelViewSet):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer

    def retrieve_patient(self, patient_id):
        response = requests.get(f'http://patients_service_url/api/patients/{patient_id}/')
        if response.status_code == 200:
            return response.json()
        return None

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
