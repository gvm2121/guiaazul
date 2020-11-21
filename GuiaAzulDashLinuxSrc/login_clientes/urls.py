from django.urls import path
from . import views

urlpatterns = [
    path('login_clientes', views.login_clientes, name='login_clientes'),   
    path('salir', views.salir, name='salir'),   
    path('mis-datos', views.mis_datos, name='mis_datos'),   
    ]