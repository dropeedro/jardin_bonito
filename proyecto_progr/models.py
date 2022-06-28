from django.db import models

# Create your models here.

class Producto(models.Model):
    idProducto = models.IntegerField(primary_key = True)
    nombreProducto = models.CharField(max_length = 60)
    precio = models.IntegerField()
    stock = models.IntegerField()
    imagen = models.ImageField()

    def __str__(self) -> str:
        return self.nombreProducto

class Promocion(models.Model):
    idPromocion = models.IntegerField(primary_key = True)
    id_producto = models.ForeignKey(Producto, on_delete = models.CASCADE)
    porc_descuento = models.IntegerField()
    fecha_caducidad = models.DateField()
    
    def __str__(self) -> str:
        return self.porc_descuento
