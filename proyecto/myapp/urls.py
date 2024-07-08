from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProduccionDiariaViewSet

router = DefaultRouter()
router.register(r'producciones', ProduccionDiariaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]