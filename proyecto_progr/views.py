from itertools import product
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import *
from .forms import *

# Create your views here.
def index(request):
    contexto = {'productos': Producto.objects.all()[:4]}
    return render(request, 'index.html', contexto)
    
def mostrarProductos(request):
    contexto = {'productos': Producto.objects.all()}
    return render(request, 'crud_productos.html', contexto)

def catalogo_productos(request):
    contexto = {'productos': Producto.objects.all()}
    return render(request, 'catalogo_productos.html', contexto)


def misCompras(request):
    return render(request, 'misCompras.html')

def login(request):
    return render(request, 'login.html')

def crearProducto(request):
    datos = {
        "form": ProductoForm()
        }
    if request.method == "POST":
        form = ProductoForm(data = request.POST, files = request.FILES)
        if form.is_valid:
            form.save()
            return redirect(to = "listar_productos")
        else:
            datos["form"] = form
    return render(request, 'crud_productos.html', datos)

def crearPromociones(request):
    datos = {
        "form": PromocionesForm()
        }
    if request.method == 'POST':
        form = PromocionesForm(data = request.POST)
        if form.is_valid:
            form.save()
            return redirect(to = "listar_promociones")
        else:
            datos["form"] = form
    return render(request, 'crud_promociones.html', datos)

def registro(request):
    form = UserRegisterForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data['username']
        messages.success(request, f'Usuario {username} ha sido creado')
        return redirect('/proyecto_progr/')
    else:
        form = UserRegisterForm()
    context = {'form':form}
    return render(request, 'registro.html', context)


## CRUD PRODUCTOS
def listarProductos(request):
    productos = Producto.objects.all()
    datos = {
        'productos' : productos
    }
    return render(request, 'listar_productos.html', datos)

def modificarProducto(request, id):
    producto = get_object_or_404(Producto, idProducto = id)
    datos = {
        'form': ProductoForm(instance = producto)
    }

    if request.method == "POST":
        formulario = ProductoForm(data = request.POST, instance = producto, files = request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to = "listar_productos")
        datos["form"] = formulario


    return render(request, 'modificar_producto.html', datos)

def eliminarProducto(request, id):
    producto = get_object_or_404(Producto, idProducto = id)
    producto.delete()
    return redirect(to = "listar_productos")


## CRUD PROMOCIONES 

def listarPromociones(request):
    promociones = Promocion.objects.all()
    datos = {
        'promociones' : promociones
    }
    return render(request, 'listar_promociones.html', datos)

def modificarPromocion(request, id):
    promociones = get_object_or_404(Promocion, idpromociones = id)
    datos = {
        'form': PromocionesForm(instance = promociones)
    }

    if request.method == "POST":
        formulario = PromocionesForm(data = request.POST, instance = promociones, files = request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to = "listar_promocioness")
        datos["form"] = formulario


    return render(request, 'modificar_promociones.html', datos)

def eliminarPromocion(request, id):
    promociones = get_object_or_404(Promocion, idPromocion = id)
    promociones.delete()
    return redirect(to = "listar_promociones")