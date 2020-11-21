from django.db import models
#from facturas.models import Listadoinicial



class SitiogaWeb(models.Model):
    libro = models.OneToOneField('facturas.Listadoinicial', models.DO_NOTHING, primary_key=True)
    oferta = models.NullBooleanField()
    novedad = models.NullBooleanField()
    saldo = models.IntegerField(blank=True, null=True)
    texto_descripcion = models.TextField(blank=True, null=True)
    descuento = models.DecimalField(max_digits=2, decimal_places=2, blank=True, null=True)
    publicar = models.BooleanField()
    destacado = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'SitioGa_web'
        
        
