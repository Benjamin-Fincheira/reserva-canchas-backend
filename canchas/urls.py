from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CanchaViewSet, ClienteViewSet, ReservaViewSet

router = DefaultRouter()
router.register(r'canchas', CanchaViewSet)# 3 endpoints
router.register(r'clientes', ClienteViewSet)
router.register(r'reservas', ReservaViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
