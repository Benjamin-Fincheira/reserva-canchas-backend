from rest_framework import viewsets
from .models import Cancha, Cliente, Reserva
from .serializers import CanchaSerializer, ClienteSerializer, ReservaSerializer

class CanchaViewSet(viewsets.ModelViewSet):#define clase con todas las operaciones crud implementadas
    queryset = Cancha.objects.all()#trae todos los registros de Cancha
    serializer_class = CanchaSerializer#indica que seralizador usar

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
