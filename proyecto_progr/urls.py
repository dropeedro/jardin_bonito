from django.urls import path
from . import views

##URLConf
urlpatterns = [
    path('', views.index, name='index'),
    path('catalogo_arbustos/', views.catalogo_arbustos, name='catalogo_arbustos'),
    path('catalogo_flores/', views.catalogo_flores, name='catalogo_flores'),
    path('catalogo_macetas/', views.catalogo_macetas, name='catalogo_macetas'),
    path('catalogo_tierra/', views.catalogo_tierra, name='catalogo_tierra'),
    path('crud_productos/', views.crearProducto, name='crud_productos'),
    path('crud_promociones/', views.crearPromociones, name='crud_promociones'),
    path('login/', views.login, name='login'),
    path('misCompras/', views.misCompras, name='misCompras'),
    path('registro/', views.registro, name='registro'),
]