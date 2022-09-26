from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = ('id', 'detalles', 'fecha', 'total', 'estado', 'proveedor')

class ProveedorSerializer(serializers.ModelSerializer):
    pedido = PedidoSerializer(many=True, read_only=True)
    class Meta:
        model = Proveedor
        fields = ('id', 'nombre', 'empresa', 'dni', 'telefono', 'cliente', 'pedido' )


class UserSerializer(serializers.ModelSerializer):
    proveedor = ProveedorSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'proveedor')