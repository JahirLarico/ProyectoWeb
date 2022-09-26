from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Proveedor(models.Model):
    cliente = models.ForeignKey(User, on_delete=models.CASCADE, related_name="proveedor")
    nombre = models.CharField(max_length=50)
    empresa = models.CharField(max_length=50)
    dni = models.IntegerField(max_length=8)
    telefono = models.IntegerField(max_length=9)

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, related_name="pedido")
    detalles = models.CharField(max_length=50)
    fecha = models.DateField()
    total = models.IntegerField(max_length=10)
    estado = models.CharField(max_length=50)

    def __str__(self):
        return self.estado
