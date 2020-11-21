from django.db import models
from django.db.models import Sum
from login_clientes.models import ClienteModel


class CarroModel(models.Model):
    fecha_agregado=models.DateTimeField(auto_now_add=True)
    cantidad=models.IntegerField()
    correo=models.CharField(max_length=50)
    producto=models.ForeignKey('facturas.Listadoinicial',unique=False,on_delete=models.CASCADE)
    
    def total(self):
        return self.cantidad * self.producto.pvp
        
    def aumentar_cantidad(self,cantidad):
        self.cantidad = self.cantidad + int(cantidad)
        self.save()
        
    def descuento(self):
        cant=self.objects.filter().aggregate(Sum('cantidad'))
        return cant

class OrdenesModel(models.Model):
    cliente=models.ForeignKey(ClienteModel,on_delete=models.CASCADE,unique=False)
    orden_numero=models.AutoField(primary_key=True)
    fecha_creacion=models.DateTimeField(auto_now_add=True)
    itemes=models.ManyToManyField(CarroModel)
    