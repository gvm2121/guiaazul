from django.urls import path
from carro.views import *


urlpatterns = [
    path('',agregar,name="agregar"),    
    path('contenido',carrovista,name="carrovista"),    
    path('resume',resume_vista,name="resume"),    
    ]

