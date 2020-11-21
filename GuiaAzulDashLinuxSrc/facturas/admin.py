from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models
from .models import FacturacionRegistro as f
from .models import Clientes,Vencimientos,Sucursales,Ventas,MovimientosBodega,Listadoinicial
from login_clientes.models import ClienteModel
#from SitioGa.models import web


'''
def sumar(modeladmin,request,queryset):
    return queryset[0]
    
sumar.short_description="sumar y filtrar"
'''
class sumaryfiltrar(admin.SimpleListFilter):
    title=("filtro personalizado")
    parameter_name = 'decade'
    
    def lookups(self,request,model_admin):
        return (('', ('seleccionado')),)
    def queryset(self,request,queryset):
        print(dir(queryset))
        print(queryset.select_related())
        return queryset


class FacturaAdmin(admin.ModelAdmin):
    formfield_overrides = {
    models.TextField: {'widget': Textarea(attrs={'rows':2, 'cols':20})},
    }
    list_display = ['folio','fecha_vencimiento','comentario','pagada','dirección','monto_total','fecha_emision','fecha_contable','fecha_pago']
    list_filter=['vencida','pagada',sumaryfiltrar,'fecha_vencimiento','fecha_pago','dirección']
    list_editable=['pagada','comentario','fecha_pago']
    

    
class ListadoinicialAdmin(admin.ModelAdmin):
    list_display=['isbn','titulo','edicion','rendir_españa']
    list_editable=['rendir_españa']
    list_filter=['rendir_españa']
    formfield_overrides = {
    models.TextField: {'widget': Textarea(attrs={'rows':1, 'cols':20})},
    }
    
    
class SucursalesAdmin(admin.ModelAdmin):
    list_display=['id','nombre','rut','direccion','comuna']

class ventasAdmin(admin.ModelAdmin):
    list_display=[]
   
"""   
class publiweb(admin.ModelAdmin):
    list_display=['isbn_','nombre', 'edicion_','oferta','publicar','destacado']
    list_filter=['libro__edicion','publicar','destacado']
    list_editable=['publicar','destacado']
    def nombre(self,obj):
        return obj.libro.titulo
    def edicion_(self,obj):
        return obj.libro.edicion
    def isbn_(self,obj):
        return obj.libro.isbn
"""    

class movimientosbodegasAdmin(admin.ModelAdmin):
    pass
class clientemodelAdmin(admin.ModelAdmin):
    pass

    
    
admin.site.register(f,FacturaAdmin)
admin.site.register(Sucursales,SucursalesAdmin)
admin.site.register(Ventas,ventasAdmin)
#admin.site.register(web,publiweb)
admin.site.register(MovimientosBodega,movimientosbodegasAdmin)
admin.site.register(Listadoinicial,ListadoinicialAdmin)
admin.site.register(ClienteModel,clientemodelAdmin)


# Register your models here.
