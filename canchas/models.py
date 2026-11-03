from django.db import models

class Cancha(models.Model):
    nombre = models.CharField(max_length=100)
    deporte = models.CharField(max_length=50) # "Futbolito", "Tenis", "Pádel"
    precioHora = models.IntegerField()
    superficie = models.CharField(max_length=100)
    capacidad = models.CharField(max_length=50)
    imagen = models.URLField(max_length=500)

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class Reserva(models.Model):
    cancha = models.ForeignKey(Cancha, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fechaClave = models.DateField() # Conectado con el formato (YYYY-MM-DD)
    hora = models.CharField(max_length=10) # "15:00", "16:00"

    def __str__(self):
        return f"Reserva: {self.cancha.nombre} - {self.fechaClave} {self.hora}"
