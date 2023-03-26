"""TerceroDjvportugal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from inicioApp import views

urlpatterns = [
    path('',views.inicioDef,name='inicioUrl'),
    path('loginAction/', views.loginSesionDef,name='loginUrl'),
    path('registarusuario/', views.registrarusuario),
    path('Clientes/', views.ClientesDef, name='Clientes'),
    path('add_cobro/',views.add_ClientesDef,name='AddCliente'),
    path('eliminarventa/', views.eliminarVenta,name='eliminarventa'),
    path('Compras/', views.ComprasDef, name='Compras'),
    path('add_Compras/', views.add_ComprasDef, name='AddCompras'),
    path('Ventas/', views.VentasDef, name='Ventas'),
    path('add_vent/', views.add_VentaDef, name='AddVentas'),
    path('admin/', admin.site.urls),
]