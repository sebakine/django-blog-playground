from django.urls import path
from . import vistas

urlpatterns = [
    path('', vistas.index, name='index'),
    path('productos/', vistas.lista_productos, name='lista_productos'),
    path('agregar-categoria/', vistas.agregar_categoria, name='agregar_categoria'),
    path('agregar-proveedor/', vistas.agregar_proveedor, name='agregar_proveedor'),
    path('agregar-producto/', vistas.agregar_producto, name='agregar_producto'),
    path('buscar/', vistas.buscar_producto, name='buscar_producto'),
    path('about/', vistas.about, name='about'),
]
