from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'index.html')

def catalogo_macetas(request):
    return render(request, 'catalogo_macetas.html')
def catalogo_flores(request):
    return render(request, 'catalogo_flores.html')
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
    return render(request, 'crud_productos.html')
def crearPromociones(request):
    return render(request, 'crud_promociones.html')