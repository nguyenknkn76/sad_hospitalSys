from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NotificationViewSet, RecipientViewSet

router = DefaultRouter()
router.register(r'notifications', NotificationViewSet)
router.register(r'recipients', RecipientViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
