import requests
from rest_framework import viewsets
from .models import Report
from .serializers import ReportSerializer

class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

    def perform_create(self, serializer):
        # Lấy dữ liệu từ các dịch vụ khác
        # 127.0.0.1:8002
        patients_response = requests.get('http://127.0.0.1:8002/api/patients/')
        appointments_response = requests.get('http://127.0.0.1:3005/api/appointments/')
        payments_response = requests.get('http://127.0.0.1:3009/api/payments/')

        # Tạo dữ liệu báo cáo
        report_data = {
            "total_patients": len(patients_response.json()),
            "total_appointments": len(appointments_response.json()),
            "total_revenue": sum(payment['amount'] for payment in payments_response.json())
        }

        # Lưu báo cáo
        serializer.save(report_data=report_data)
