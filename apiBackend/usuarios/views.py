from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import *
from .serializers import *
# Create your views here.

class IndexView(APIView):
    def get(self, request):
        return Response("Servidor Activo")

class UserList(APIView):
    def get(self, request):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializers = UserSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)

class UserDetail(APIView):
    def get(self, request):
        username = request.GET.get('nombreUsuario', '')
        user = User.objects.get(username=username)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    def put(self, request):
        username = request.GET.get('nombreUsuario', '')
        user = User.objects.get(username=username)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class ProveedorList(APIView):
    def get(self, request):
        proveedor = Proveedor.objects.all()
        serializer = ProveedorSerializer(proveedor, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializers = ProveedorSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)

class ProveedoresByUser(APIView):
    def get(self, request):
        idCliente = request.GET.get('idCliente', '')
        proveedor = Proveedor.objects.filter(cliente=idCliente)
        serializer = ProveedorSerializer(proveedor, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializers = ProveedorSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)

class ProveedorEdit(APIView):
    def get(self, request):
        idCliente = request.GET.get('idCliente', '')
        nombreProveedor = request.GET.get('nombreProveedor', '')
        proveedor = Proveedor.objects.get(cliente=idCliente,nombre=nombreProveedor)
        serializer = ProveedorSerializer(proveedor)
        return Response(serializer.data)
    def put(self, request):
        idCliente = request.GET.get('idCliente', '')
        nombreProveedor = request.GET.get('nombreProveedor', '')
        proveedor = Proveedor.objects.get(cliente = idCliente ,nombre=nombreProveedor)
        serializer = ProveedorSerializer(proveedor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    def delete(self, request):
        idCliente = request.GET.get('idCliente', '')
        nombreProveedor = request.GET.get('nombreProveedor', '')
        proveedor = Proveedor.objects.get(cliente = idCliente ,nombre=nombreProveedor)
        proveedor.delete()
        return Response("Proveedor eliminado")

class PedidoList(APIView):
    def get(self, request):
        pedido = Pedido.objects.all()
        serializer = PedidoSerializer(pedido, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializers = PedidoSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)

class PedidoByProveedor(APIView):
    def get(self, request):
        nombreProveedor = request.GET.get('nombreProveedor', '')
        proveedor = Proveedor.objects.get(nombre=nombreProveedor)
        pedido = Pedido.objects.filter(proveedor=proveedor)
        serializer = PedidoSerializer(pedido, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializers = PedidoSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)

class PedidoEdit(APIView):
    def get(self , request):
        idProveedor = request.GET.get('idProveedor', '')
        idPedido = request.GET.get('idPedido', '')
        pedido = Pedido.objects.get(proveedor=idProveedor ,id=idPedido)
        serializer = PedidoSerializer(pedido)
        return Response(serializer.data)
    def put(self, request):
        idProveedor = request.GET.get('idProveedor', '')
        idPedido = request.GET.get('idPedido', '')
        pedido = Pedido.objects.get(proveedor=idProveedor ,id=idPedido)
        serializer = PedidoSerializer(pedido, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    def delete(self, request):
        idProveedor = request.GET.get('idProveedor', '')
        idPedido = request.GET.get('idPedido', '')
        pedido = Pedido.objects.get(proveedor=idProveedor ,id=idPedido)
        pedido.delete()
        return Response("Pedido eliminado")