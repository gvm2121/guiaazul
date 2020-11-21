from django.db import models

# Create your models here.

class ClienteModel(models.Model):
    id=models.AutoField(primary_key=True)
    rut=models.TextField()
    password=models.TextField()
    nombre=models.TextField()
    correo=models.TextField()
    direccion_envio=models.TextField(default='')
    comuna_despacho=models.TextField()
    
    class Meta:
        managed=True
    

