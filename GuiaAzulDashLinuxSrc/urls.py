from django.urls import path
from carro_compras.views import *


urlpatterns = [
    path('',agregar,name="agregar"),    
    path('contenido',carrovista,name="carrovista"),    
    path('resume',resume_vista,name="resume"),    
    ]

