from django.shortcuts import render
# from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.
def index(request):
    contexto = {'productos': Producto.objects.all()}
    return render(request, 'index.html', contexto)
    
def mostrarProductos(request):
    contexto = {'productos': Producto.objects.all()}
    return render(request, 'crud_productos.html', contexto)

def catalogo_macetas(request):
    return render(request, 'catalogo_macetas.html')

def catalogo_flores(request):
    contexto = {'productos': Producto.objects.all()}
    return render(request, 'catalogo_flores.html', contexto)

def catalogo_arbustos(request):
    return render(request, 'catalogo_arbustos.html')

def catalogo_tierra(request):
    return render(request, 'catalogo_tierra.html')

def misCompras(request):
    return render(request, 'misCompras.html')

def login(request):
    return render(request, 'login.html')
def registro(request):
    return render(request, 'registro.html')


def crearProducto(request):
    datos = {
        "form": ProductoForm()
        }
    if request.method == "POST":
        form = ProductoForm(data = request.POST, files = request.FILES)
        if form.is_valid:
            form.save()
            datos["mensaje"] = "Producto Agregado"
        else:
            datos["form"] = form
    return render(request, 'crud_productos.html', datos)

def crearPromociones(request):
    return render(request, 'crud_promociones.html')
        