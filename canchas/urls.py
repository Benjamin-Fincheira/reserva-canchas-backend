from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CanchaViewSet, ClienteViewSet, ReservaViewSet

router = DefaultRouter()#genera todas las rutas posibles del CRUD
router.register(r'canchas', CanchaViewSet)# 3 endpoints
router.register(r'clientes', ClienteViewSet)
router.register(r'reservas', ReservaViewSet)
#conecta la direccion web con una vista, la cual consulta la base de datos y entrega los datos en formato JSON
urlpatterns = [#toma todas las rutas generadas y agrega prefijo api/
    path('api/', include(router.urls)),#para catalogarlas como rutas que responden a datos en formato JSON
] 
