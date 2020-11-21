from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect,HttpRequest
from .formularios import login_cliente,cliente_nuevo_form
from .models import ClienteModel

def login_clientes(request):
    contexto={}
    formulario=login_cliente()
    formulario_cliente_nuevo=cliente_nuevo_form()
    contexto['logeo']=request.session['logeo']=False
    contexto['formulario']=formulario
    contexto['formulario_cliente_nuevo']=formulario_cliente_nuevo
    contexto['todos']=ClienteModel.objects.all() #auxiliar para ver los login de prueba, se debe borrar en producttion
    if request.method=='POST':
        fl=login_cliente(request.POST)
        if fl.is_valid():
            correo=fl.cleaned_data['correo']
            password=fl.cleaned_data['password']
            if ClienteModel.objects.filter(correo=correo,password=password):
                contexto['logeo']=request.session['logeo']=True
                contexto['correo']=request.session['correo']=correo
                
                return redirect('home')
    return render(request,'login_clientes/login_clientes.html',contexto)

def salir(request):
    request.session['logeo']=False
    try:
        request.session['correo']=''
    except:
        pass
    return HttpResponseRedirect('/')
    
def mis_datos(request):
    print(request.session['correo'])
    #datos_cliente=ClienteModel.objects.all()
    datos_cliente=ClienteModel.objects.get(correo=request.session['correo'])
    #print(dir(datos_cliente))
    print(datos_cliente)
    #datos_cliente=ClienteModel.objects.all()
    datos=cliente_nuevo_form(instance=datos_cliente)
    return render(request,'login_clientes/mis_datos.html',{'datos':datos,'logeo':request.session['logeo'],'correo':request.session['correo']})    