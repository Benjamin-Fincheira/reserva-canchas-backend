from rest_framework import serializers
from .models import Cancha, Cliente, Reserva

class CanchaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cancha
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'

    # Validar que no se dupliquen reservas a la misma hora
    def validate(self, data):
        cancha = data.get('cancha')
        fechaClave = data.get('fechaClave')
        hora = data.get('hora')

        # Si ya existe una reserva con la misma cancha, fecha y hora, lanzamos error
        if Reserva.objects.filter(cancha=cancha, fechaClave=fechaClave, hora=hora).exists():
            raise serializers.ValidationError({
                "hora": "Esta cancha ya se encuentra reservada en el horario seleccionado."
            })
        return data
