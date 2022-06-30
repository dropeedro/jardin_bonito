from django.urls import path
from . import views

##URLConf
urlpatterns = [
    path('', views.index, name='index'),
    path('catalogo_productos/', views.catalogo_productos, name='catalogo_productos'),
    path('crud_productos/', views.crearProducto, name='crud_productos'),
    path('crud_promociones/', views.crearPromociones, name='crud_promociones'),
    path('login/', views.login, name='login'),
    path('misCompras/', views.misCompras, name='misCompras'),
    path('registro/', views.registro, name='registro'),
]