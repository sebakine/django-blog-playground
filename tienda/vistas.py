from django.shortcuts import render, redirect
from .modelos import Producto, Categoria, Proveedor
from .formularios import ProductoFormulario, CategoriaFormulario, ProveedorFormulario

def index(request):
    return render(request, 'tienda/index.html')

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'tienda/productos.html', {'productos': productos})

def agregar_categoria(request):
    if request.method == 'POST':
        formulario = CategoriaFormulario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('index')
    else:
        formulario = CategoriaFormulario()
    return render(request, 'tienda/agregar_categoria.html', {'formulario': formulario})

def agregar_proveedor(request):
    if request.method == 'POST':
        formulario = ProveedorFormulario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('index')
    else:
        formulario = ProveedorFormulario()
    return render(request, 'tienda/agregar_proveedor.html', {'formulario': formulario})

def agregar_producto(request):
    if request.method == 'POST':
        formulario = ProductoFormulario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('lista_productos')
    else:
        formulario = ProductoFormulario()
    return render(request, 'tienda/agregar_producto.html', {'formulario': formulario})

def buscar_producto(request):
    busqueda = request.GET.get('q', '')
    if busqueda:
        resultados = Producto.objects.filter(nombre__icontains=busqueda)
    else:
        resultados = []
    
    return render(request, 'tienda/buscar.html', {'resultados': resultados, 'busqueda': busqueda})

def about(request):
    return render(request, 'tienda/about.html')
