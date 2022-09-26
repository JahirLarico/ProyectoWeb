from django import urls
from django.urls import path
from . import views

app_name = "usuarios"

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    
    #USUARIO
    path('usuarios', views.UserList.as_view(), name="usuarios"),
    path('usuarioDetail', views.UserDetail.as_view(), name="usuarioDetail"),
    # usuarioDetail?nombreUsuario=admin

    #PROVEEDOR
    path('proveedores', views.ProveedorList.as_view(), name="proveedores"),
    path('proveedoresByUser', views.ProveedoresByUser.as_view(), name="proveedoresByUser"),
    # proveedoresByUser?nombreUsuario=admin

    path('proveedorEdit', views.ProveedorEdit.as_view(), name="proveedorEdit"),
    #proveedorEdit?nombreProveedor=Jahir&idCliente=1

    #PEDIDO
    path('pedidos', views.PedidoList.as_view(), name="pedidos"),
    path('pedidosByProveedor', views.PedidoByProveedor.as_view(), name="PedidoByProveedor"),
    # pedidosByProveedor?nombreProveedor=Jahir

    path('pedidoEdit', views.PedidoEdit.as_view(), name="pedidoEdit"),
    #pedidoEdit?idProveedor=1&idPedido=1

    #GENERAL
    path('usuarios', views.UserList.as_view(), name="usuarios"),
    path('proveedores', views.ProveedorList.as_view(), name="proveedores"),
    path('pedidos', views.PedidoList.as_view(), name="pedidos"),
]