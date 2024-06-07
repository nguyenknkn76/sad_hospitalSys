from django.shortcuts import HttpResponse
import requests

def auth_service_proxy(request):
    url = 'http://127.0.0.1:8000/api/auth/'  # URL của dịch vụ xác thực
    response = requests.get(url)
    return HttpResponse(response.content)
