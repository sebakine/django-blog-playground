from django.contrib import admin
from .modelos import Producto, Categoria, Proveedor

admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Proveedor)
