from re import template
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

##URLConf
urlpatterns = [
    path('', views.index, name='index'),
    path('catalogo_productos/', views.catalogo_productos, name='catalogo_productos'),
    path('crud_productos/', views.crearProducto, name='crud_productos'),
    path('crud_promociones/', views.crearPromociones, name='crud_promociones'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('misCompras/', views.misCompras, name='misCompras'),
    path('registro/', views.registro, name='registro'),
]