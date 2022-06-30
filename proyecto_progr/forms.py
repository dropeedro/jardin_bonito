from dataclasses import fields
from django.forms import ModelForm
from .models import *

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = [
                'idProducto',
                'nombreProducto',
                'descripcion',
                'precio',
                'stock',
                'imagen'
                ]

class PromocionesForm(ModelForm):
    class Meta:
        model = Promocion
        fields = [
            'idPromocion',
            'id_producto',
            'porc_descuento',
            'fecha_caducidad',
        ]