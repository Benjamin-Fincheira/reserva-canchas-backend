from django.db import models

class Cancha(models.Model):
    nombre = models.CharField(max_length=100)
    deporte = models.CharField(max_length=50) # "Futbolito", "Tenis", "Pádel"
    precioHora = models.IntegerField()
    superficie = models.CharField(max_length=100)
    capacidad = models.CharField(max_length=50)
    imagen = models.URLField(max_length=500, blank=True, null=True) #exige que sea una direccion web valida (http://) y la imagen es opcional

    def __str__(self):
        return self.nombre #muestra el nombre de la cancha en el sistema

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)#evita correos duplicados en diferentes clientes
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre #muestra el nombre del cliente en el sistema

class Reserva(models.Model):
    cancha = models.ForeignKey(Cancha, on_delete=models.CASCADE)#Cascade elimina todas las reservas en esa cancha al eliminar la cancha
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)#Cascade elimina todas las reservas del cliente al eliminar el cliente
    fechaClave = models.DateField() # Conectado con el formato (YYYY-MM-DD)
    hora = models.CharField(max_length=10) 
class Meta: #esta clase con este nombre en especifico le da ordenes especificas a Django en la clase Reserva
    ordering = ['-fechaClave', 'hora']#ordena las reservas mostradas desde la mas reciente a la mas antigua
    
    def __str__(self):
        return f"Reserva: {self.cancha.nombre} - {self.fechaClave} {self.hora}"
    #Devuelve un formato tipo: "Reserva: Cancha Pasto Sintético #1 - 2026-11-20 18:00"
