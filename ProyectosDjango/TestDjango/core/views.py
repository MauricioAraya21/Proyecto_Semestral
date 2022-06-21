from django.shortcuts import redirect, render
from .forms import formularioForm
from core.Carrito import Carrito
from core.models import Producto
# Create your views here.

def index(request):
    return render(request, 'index_central.html')

def tienda(request):
    productos = Producto.objects.all()
    return render(request, "tienda.html", {'productos':productos})

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("Tienda")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("Tienda")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("Tienda")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("Tienda")

def formulario(request):
    data = {
        'form': formularioForm()
    }

    if request.method == 'POST':
        formulario = formularioForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "formulario guardado"
        else:
            data["form"] = formulario

    return render(request, 'formulario.html',data)