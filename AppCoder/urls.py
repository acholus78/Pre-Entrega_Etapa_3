from django.urls import path, include
from AppCoder import views


urlpatterns = [
    path ('', views.inicio, name ="Inicio"),
    path ('productos', views.productos, name ="Productos"),
    path ('clientes', views.clientes, name ="Clientes"),
    path ('proveedores', views.proveedores, name ="Proveedores"),
    path ('clienteFormulario', views.clienteFormulario, name="ClienteFormulario"),
    path ('busquedaProducto', views.busquedaProducto, name="BusquedaProducto"),
    path ('buscar/', views.buscar),
]