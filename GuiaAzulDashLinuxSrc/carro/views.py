from django.shortcuts import render,redirect,get_object_or_404,get_list_or_404
from .formularios import formulariocantidad
from SitioGa.forms import FormularioContacto
from login_clientes.models import ClienteModel
from django.shortcuts import render
from carro.models import CarroModel,OrdenesModel
from facturas.models import Listadoinicial
from django.db.models import Sum
from django.contrib import messages as m
from django.db.models import Sum
from login_clientes.formularios import cliente_nuevo_form
import decimal

#ESTA DEBERÍA SER AGREGAR AL CARRO Y NO VINCULA A NINGUNA VISTA, SOLO AFECTA LA BASE DE DATOS
def agregar(request):
    f=formulariocantidad(request.POST)
    if f.is_valid():
        try:
            existe=CarroModel.objects.get(correo=request.session['correo'],producto=request.session['isbn'])
            existe.cantidad=existe.cantidad + int(f.cleaned_data['cantidad'])
            existe.save()
        except:
            c=CarroModel()
            c.cantidad=f.cleaned_data['cantidad']
            c.correo=request.session['correo']
            c.producto=Listadoinicial(isbn=request.session['isbn'])
            c.save()
        m.add_message(request, m.SUCCESS, 'Agregado al carro')
        return redirect('detalle', i=request.session['isbn'])
    
    
def carrovista(request):
    if request.session['logeo']:
        context={}
        context['logeo']=request.session['logeo']
        context['correo']=request.session['correo']
        if CarroModel.objects.filter(correo=request.session['correo']):
            context['hay_productos']=True
            context['productos']=CarroModel.objects.filter(correo=request.session['correo'])
            context['subtotal']=subtotal_del_carro(request)
            context['descuento']=descuento(request)
            context['total']=total(request) 
            
        else:
            context['hay_productos']=False
            
        
        if request.method=='POST':
            postdata=request.POST.copy()
            
            if postdata['submit']=='Update':
                update_cart(request)
            if postdata['submit']=='Remove':
                borrar_del_carro(request)
                print('revisaremos el contexto',context)
            context['hay_productos']=revisar_contenido_carro(request)    
            context['subtotal']=subtotal_del_carro(request)
            context['descuento']=descuento(request)
            context['total']=total(request)
               
            
        return render(request,'carro/carro.html',context)
    return redirect('login_clientes')
    
def update_cart(request):
    postdata=request.POST.copy()
    item_id=postdata['item_id']
    cantidad=postdata['quantity']
    cart_item=get_single_item(request,item_id)
    
    if cart_item:
        if int(cantidad)>0:
            cart_item.update(cantidad=cantidad)
        else:
            borrar_del_carro(request)
            
def get_single_item(request,item_id):
    c=CarroModel.objects.filter(producto=item_id,correo=request.session['correo'])
    return c
   

def borrar_del_carro(request):
    postdata=request.POST.copy()
    item_id=postdata['item_id']
    cart_item=get_single_item(request,item_id)
    if cart_item:
        cart_item.delete()

def subtotal_del_carro(request):
    subtotal=0
    productos=CarroModel.objects.filter(correo=request.session['correo'])
    for p in productos:
        subtotal += p.producto.pvp*p.cantidad
    return subtotal
def descuento(request):
    try:
        cant=CarroModel.objects.filter(correo=request.session['correo']).aggregate(Sum('cantidad'))
        q=cant['cantidad__sum']
        if q==1 or q==0:
            return 0
        if q==2:
            return 0.05
        if 3<= q <=4:
            return 0.11
        if q>=5:
            return 0.13
    except:
        return 0
def total(request):
    total=decimal.Decimal()
    total=subtotal_del_carro(request)*(1-decimal.Decimal(descuento(request)))
    return int(total)
def revisar_contenido_carro(request):
    if CarroModel.objects.filter(correo=request.session['correo']):
        return True
    else:
        return False


def resume_vista(request):
    orden=OrdenesModel()
    orden.save()
    orden.cliente=ClienteModel.objects.get(correo=request.session['correo'])
    for i in CarroModel.objects.filter(correo=request.session['correo']):
        orden.itemes.add(i)
    
    context={'orden':orden}
    return render(request,'carro/resume.html',context)
    

