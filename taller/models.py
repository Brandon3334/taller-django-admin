from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=12, unique=True)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField()
    fecha_registro = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} - {self.rut}"


class Reparacion(models.Model):
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name="reparaciones"
    )
    vehiculo = models.CharField(max_length=100)
    descripcion = models.TextField()
    costo = models.PositiveIntegerField()
    fecha_ingreso = models.DateField()
    terminada = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.vehiculo} - {self.cliente.nombre}"