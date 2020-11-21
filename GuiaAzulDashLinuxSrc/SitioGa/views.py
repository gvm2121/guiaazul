from django.http import HttpResponseRedirect
from django.shortcuts import render
from facturas.models import StockBodega as saldo
from facturas.models import Listadoinicial 
from SitioGa.views import *
from SitioGa.forms import FormularioContacto
from django.core.mail import EmailMessage
from .models import SitiogaWeb as web
import os, fnmatch,pdb,re
from random import shuffle
from .funciones_externas import libro_objeto
from carro.formularios import formulariocantidad
from django.contrib import messages as m 
catalogo=web.objects.filter(publicar=True)
destacados=web.objects.filter(destacado=True)
form=FormularioContacto()
context={}
BASE_DIR2=os.path.join(os.getcwd(),'SitioGa','Templates','SitioGa')
d=os.listdir(path=BASE_DIR2)

def home(request):
    libros_destacados=[]
    #print('ESTA ES EN EL INDEX',request.session['logeo'])
    try:
        if request.session['logeo']:
            context['correo']=request.session['correo']
            context['logeo']=request.session['logeo']
        else:
            context['logeo']=request.session['logeo']=False
            del context['correo']
            
    except KeyError:
        request.session['logeo']=False
        request.session['correo']=''
        #context['logeo']=False
        pass
     
    for d in destacados:
        libros_destacados.append(libro_objeto(d.libro.isbn))
     
    if form.is_valid():
        form.save()
    context['catalogo']=catalogo
    context['form']=form
    context['libros_destacados']=libros_destacados
    
    return render(request,'SitioGa/prueba.html', context)
    



def guia2(request,i):
    mensaje=False
    request.session['isbn']=i
    ejemplar=libro_objeto(str(i))
    if m.get_messages(request):
        mensaje=m.get_messages(request)
    return render(request, 'SitioGa/r4.html',{'form':form,'ejemplar':ejemplar,'catalogo':catalogo,'logeo':request.session['logeo'],'correo':request.session['correo'],'formulario_cantidad':formulariocantidad(),'mensaje':mensaje})
	

	
def contacto(request):
    if request.method == 'POST':
        form=FormularioContacto(request.POST)
        if form.is_valid():
            error=False
            nombre = form.cleaned_data['Nombre']
            pais=form.cleaned_data['Pais']
            mensaje = form.cleaned_data['Mensaje']
            sender = form.cleaned_data['Email']
            body='han enviaso desde %s el siguiente mensaje : %s' %(sender,mensaje)
            mgs=EmailMessage('***CONTACTO DESDE SITIO WEB',body,sender,['guiaazulchile@gmail.com',],reply_to=[sender])
            mgs.send()
            
            #send_mail('*** CONTACTO DESDE SITIO WEB ***', sender,sender,['gvm2121@gmail.com'],)
            return render(request,'SitioGa/gracias.html',{'libros':libros,'error':error})
        else:
            error=True
            return render(request,'SitioGa/gracias.html',{'libros':libros,'error':error,'form':form})
            
    return HttpResponseRedirect('MAL')

def qs(request):
    
    return render(request,'SitioGa/qs.html',{'form':form,'catalogo':catalogo,'logeo':request.session['logeo'],'correo':request.session['correo']})

def de(request):
    
    return render(request,'SitioGa/de.html',{'form':form,'catalogo':catalogo,'logeo':request.session['logeo'],'correo':request.session['correo']})




# Create your views here.
