from django import forms
from django.forms import ModelForm,TextInput,DateInput,SelectDateWidget,Select,formset_factory,RadioSelect,SelectMultiple
from .models import MovimientosBodega,VentasContrapuntoPilgrim, FacturacionRegistro


codigos_sucursal=(
(600,'Pilgrim'),
(200,'Mandiola'),(100,'Fch'),
(501,'contrapunto huérfanos'),(502,'contrapunto Plaza Egaña'),
(503, 'Contrapunto Trébol'),
(504, 'Contrapunto Casa Costanera'),
(505, 'Contrapunto La Dehesa '),
(400, 'Buscalibre'),
)    

class tablaVCPFormulario(ModelForm):
    class Meta:
        model=VentasContrapuntoPilgrim
        fields='__all__'
        widgets = {
           'titulo': TextInput,
           'edicion': TextInput,
           'fecha_contable':SelectDateWidget(attrs={'class': 'custom-select'}),
           'cod_sucursal':Select(choices=codigos_sucursal),
        }
        exclude = ('saldo','inicial')
        prefix='encabezado'
        
class VentasDeTiendasNoTradicionales(forms.Form):
    isbn=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','type':'text'}))
    venta=forms.IntegerField(widget=forms.Textarea(attrs=({'class':'form-control','rows': '1','cols': '4'})))
    descripcion=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    prefix='detalle'

    
VentasFormSet=formset_factory(VentasDeTiendasNoTradicionales,extra=30)
        
class facturas_filtradas_modelform(forms.ModelForm):
    class Meta:
        model=FacturacionRegistro
        fields=('folio','fecha_vencimiento','monto_total','pagada','fecha_pago','otros_comentarios')
