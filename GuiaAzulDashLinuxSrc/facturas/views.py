from django.shortcuts import render
from django.db.models import Sum,Max,Q
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect,HttpRequest
from django.template import loader
from django.core import serializers
from .models import FacturacionRegistro,TablaCantidadTienda 
from facturas.models import Ventas as v
from .models import Sucursales as s
from .models import StockBodega as SB
from .models import FaltantesTabla as FA
from .models import MovimientosBodega as mo
from .models import VentasContrapuntoPilgrim as vcp
from .models import GuiasDespacho as gd
from .models import ArqueoOct2018 as arq
from facturas.models import Listadoinicial as l 
from .forms  import tablaVCPFormulario,VentasFormSet
from django.contrib.auth.decorators import login_required
import csv
import gviz_api
import json
import psycopg2
import os


@login_required
def exportar_facturas_impagas_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="facturas_impagas.csv"'
    impagas= FacturacionRegistro.objects.filter(pagada=False,vencida=True,tipo_documento=33).order_by('fecha_vencimiento')
    for impaga in impagas.values():
        campos=[t for t in impaga]
    writter = csv.DictWriter(response,fieldnames=campos,dialect="excel",delimiter=";")
    writter.writeheader()
    for impaga in impagas.values():
        writter.writerow(impaga)
    

    return response

@login_required    
def csv_stock(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="stock.csv"'
    que=SB.objects.order_by('-stock')
    for q in que.values():
        campos=[t for t in q]
    writter = csv.DictWriter(response,fieldnames=campos,dialect="excel",delimiter=";")
    writter.writeheader()
    for q in que.values():
        writter.writerow(q)
    

    return response




@login_required
def index(request):
            
    facturas = FacturacionRegistro.objects.raw('''select 300000 as "id", facturacion_registro.fecha_contable as fecha ,sum(facturacion_registro."Monto_neto")::numeric as m, sum(facturacion_registro."Utilidad")::numeric as u from facturacion_registro where tipo_documento=33 group by fecha_contable order by fecha_contable asc''')
    stock_mercado=v.objects.raw('''select 1 as id_number,"FECHA" as fecha ,sum("SALDO") as c,sum("VENTA") as ve from ventas group by "FECHA" order by "FECHA" asc  ''')
    stock_por_tiendas=TablaCantidadTienda.objects.all()
    tiendas=s.objects.all()
    
    ventas_historicas=v.objects.raw(''' select 1 as id_number,"FECHA" as f ,sum("VENTA") as ve,sum("LIQUIDACION")::numeric as s from ventas group by "FECHA" order by "FECHA" asc; ''')

    #for imp in impagas:
    #    ultima_act=imp.ultima_actualizacion
    #    break
    
    
    #for sumatoria in sumas.values():
    #   suma=sumatoria
      
    context = {
        'facturas': facturas,'stock_mercado':stock_mercado,'stock_por_tiendas':stock_por_tiendas, 'tiendas':tiendas,'ventas_historicas':ventas_historicas
    }

    return render(request,'facturas/index.html',context)
     
@login_required
def datos(request,cod_suc):
    
    if cod_suc==0:
        edad_stock=v.objects.raw('''select 1 as id_number, sum("SALDO") as s ,l."EDICION" as edi from ventas v join listadoinicial l on l."ISBN"=v."ISBN" where v."FECHA"=(select max(v."FECHA") from ventas v) group by l."EDICION" ''')
    else:
        edad_stock=v.objects.raw('''select 1 as id_number, sum("SALDO") as s ,l."EDICION" as edi from ventas v join listadoinicial l on l."ISBN"=v."ISBN" where v."FECHA"=(select max(v."FECHA") from ventas v) and "COD_SUCURSAL"=%s group by l."EDICION" ''',[cod_suc])
  
    datos_aux={}
    datos=[]
    
    for e in edad_stock:       
        datos_aux["saldo"]=int(e.s)
        datos_aux["edicion"]=e.edi
        datos.append(datos_aux)
        datos_aux={}
        
   
    
    description2={"saldo":("number","saldo"),"edicion":("string","edicion")}
    data_table = gviz_api.DataTable(description2)
    data_table.LoadData(datos)
    j=data_table.ToJSon(columns_order=("edicion", "saldo"))
   
    
    return HttpResponse(j, content_type='application/json') 

@login_required
def vista_stock(request):
    max_fecha=SB.objects.all().aggregate(Max('ultima_actualizacion'))
    #print(dir(max_fecha))
    for k in max_fecha.values():
        k=k
    
    stock_bodegas=SB.objects.filter(ultima_actualizacion=k,stock__gt=0).order_by('-stock')
   
    edad_stock_bodega=SB.objects.raw('''select 1 as id, "_edicion" as edi , sum("stock") as s  from stock_bodega where stock>0 group by _edicion''')
    ultimas_guias=mo.objects.raw(''' select distinct on (numero_guia_factura) numero_guia_factura as num ,fecha as f, destino as d,1 as unico from movimientos_bodega where salida_ingreso ilike 'salida' and numero_guia_factura is not null and numero_guia_factura<>'' order by numero_guia_factura desc ''')[0:20]
    
    context={'stock_bodegas':stock_bodegas,'edad_stock_bodega':edad_stock_bodega,'k':k,'ultimas_guias':ultimas_guias}
    return render(request,'facturas/stock.html',context)

@login_required
def analisis_sucursal(request):
    #listado de ultimos enviados
    #mas vendidos historicos select sum("VENTA"),"DESCRIPCION" from ventas v where
    #  v."COD_SUCURSAL"=100 group by "VENTA","DESCRIPCION" order by sum("VENTA") DESC 
    #ultimas ventas
    #en qué sucursal el stock está más viejo?
    #que libros faltan y son mas vendidos
    #falta=v.objects.raw(''' select 1 as id_number, _bosa as bosa, _isbn as isbn, _nombre as nombre, _edicion as edicion, _costo_tienda as costo_tienda from llenar_tiendas(311,4,2018);''')
    
    #mas vendidos sucursal
    #select "ISBN","DESCRIPCION",SUM("VENTA") from ventas where "COD_SUCURSAL"=304  
    #GROUP BY "ISBN","DESCRIPCION", "VENTA" ORDER BY SUM("VENTA") desc
    tiendas=s.objects.all()
    dic_faltantes=[]
    aux={}
    for tienda in tiendas:
        falta=FA.objects.filter(tienda=tienda.id,saldo_bodega__gt=0)
        aux['tienda_id']=tienda.id
        aux['nombre_sucursal']=tienda.nombre
        aux['cantidad_faltante']=falta.count()
        aux['falta']=falta
        dic_faltantes.append(aux)
        aux={}
    
    
    
    #acá hay que hacer un gran diccinario o lista
    #que contenta todo [{'nombre':mombre_suc,'faltantes':queryconfaltantes,'cantidad':cuantos_faltan}]   
    ultima_fechas=FA.objects.all().aggregate(Max('fecha_contable'))
    
    for u in ultima_fechas.values():
        u=u

            
    
    context={'tiendas':tiendas, 'faltantes':dic_faltantes,'u_f':u}
    
    return render(request,'facturas/analisis_sucursal.html',context)

@login_required
def analisis_titulo(request):
    return render(request,'facturas/analisis_titulo.html')

@login_required    
def csv_sucursal(request,nombre_sucursal):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename='+ nombre_sucursal+'.csv'
    codigo_sucursal=s.objects.get(nombre=nombre_sucursal) #get obtiene solo uno
    falta=FA.objects.filter(tienda=codigo_sucursal.id)
    for q in falta.values():
        campos=[t for t in q]
    writter = csv.DictWriter(response,fieldnames=campos,dialect="excel",delimiter=";")
    writter.writeheader()
    for q in falta.values():
        writter.writerow(q)
    
    
    return response

@login_required
def historico(request):
    historicos=v.objects.raw(''' ''')
    context={'historicos':historicos}
    return render(request,'facturas/historico.html',context)

@login_required    
def busqueda(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        precio=l.objects.filter(titulo__icontains=q)
        results = []
        for p in precio:
            p_json = {}
            #p_json['value']=p.isbn
            p_json['label']=p.titulo #para que funcione debe llevar un campo label y un value
            results.append(p_json)
            
        data=json.dumps(results)
        
    else:
        data='fail'
                 
            
    
    return HttpResponse(data,'application/json')

@login_required
def tablaventas(request):
    formulario=tablaVCPFormulario(prefix='encabezado',auto_id=True)
    VentasFormSet2=VentasFormSet(prefix='detalle')
    context={'formulario':formulario,'VentasFormSet2':VentasFormSet2}
    return render(request,'facturas/tablaventas.html',context)

@login_required    
def busqueda_isbn(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        
        #isbn_unico=l.objects.filter(isbn__icontains=q)
        isbn_unico=l.objects.filter(Q(isbn__icontains=q)|Q(titulo__icontains=q))
        
        results = []
        for p in isbn_unico:
            p_json = {}
            #p_json['value']=p.isbn
            p_json['label']=p.isbn+' '+p.titulo #para que funcione debe llevar un campo label y un value
            p_json['desc']=p.isbn
            
            results.append(p_json)
            
        data=json.dumps(results)
        
    else:
        data='fail'
                 
            
    print(data)
    return HttpResponse(data,'application/json')

@login_required
def tablaventas_recibo(request):
    datos={}
    if request.method=='POST':
        formu=VentasFormSet(request.POST, prefix='detalle') # formset 
        encabezado=tablaVCPFormulario(request.POST, prefix='encabezado') # Formulario
        
        if formu.is_valid() and encabezado.is_valid():
            
           
            datos['cod_sucursal']=encabezado.cleaned_data['cod_sucursal']
            datos['fecha_contable']=encabezado.cleaned_data['fecha_contable']
            
            for detalle in formu:
                d=detalle.cleaned_data
                
                if d.get('isbn') is not None:
                    datos['isbn']=str(d.get('isbn'))
                    datos['venta']=d.get('venta')
                    
                    formu2=tablaVCPFormulario(datos)
                    formu2.save()
                    
               
            
            return HttpResponse('TOdo_bien')
            
            
    return HttpResponse(encabezado.errors)

    

def analisis_sucursal_historico(request,cod_suc_2):
    sucursal_historico=v.objects.raw(''' select 1 as id_number, sum("VENTA") as ve ,sum("SALDO") as sa ,"FECHA" as fe from ventas v where "COD_SUCURSAL"=%s group by "FECHA" order by "FECHA" asc ''',[cod_suc_2])
    datos_aux={}
    datos=[]
    for e in sucursal_historico:       
        datos_aux["fecha"]=e.fe
        datos_aux["venta"]=int(e.ve)
        datos_aux["saldo"]=int(e.sa)
        datos.append(datos_aux)
        datos_aux={}    
    description2={"fecha":("string","fecha"),"venta":("number","venta"),"saldo":("number","saldo")}
    data_table = gviz_api.DataTable(description2)
    data_table.LoadData(datos)
    j=data_table.ToJSon(columns_order=("fecha","venta", "saldo"))   
    
    return HttpResponse(j) 

@login_required    
def buscalibre_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="buscalibre.csv"'
    que=SB.objects.raw(''' select id,  s."_isbn" as ISBN, s."_titulo" as TITULO, s."_edicion" as EDICION,s."stock" as stock,l."PVP" as PVP, l."PVP"/1.19 as Precio_Neto from stock() s join listadoinicial l on s."_isbn"=l."ISBN" where s."stock">0; ''')
    fila=que.__getitem__(2).__dict__
    fila2=list(fila.keys())
    fila2.remove('_state')
    fila2.remove('id')
    writter = csv.DictWriter(response,fieldnames=fila2,dialect="excel",delimiter=";")
    writter.writeheader()
    for q in que:
        del q.__dict__['_state']
        del q.__dict__['id']
        writter.writerow(q.__dict__)
    return response
    
def mas_vendidos(request):
    return HttpResponse("Los más vendidos ordenados por fecha")
    

def ratios(request):
    return HttpResponse(" aca van los ratios por sucursal y fecha ")
    
def validador_facturas(request):
    
    fechas=v.objects.distinct("fecha").order_by("-fecha")
    context={'fechas':fechas}
    return render(request,'facturas/revision_facturas.html',context)
    
def validador_facturas_salida(request,fecha):
    tablas=SB.objects.raw(''' select 1 as id,s."ID" as sucursal ,s."NOMBRE" as nombre_sucursal,f."Folio" as folio,sum(f."Monto_neto") as suma_factura,sum(ve.suma) as suma_liquidacion,f.fecha_contable as fecha_factura_contable 
from sucursales s 
	left join facturacion_registro f on s."ID"=f."Cod_sucursal" and f.fecha_contable=%s 
	left join (select v."COD_SUCURSAL",sum(v."LIQUIDACION") as suma ,v."FECHA" from ventas v where v."FECHA"=%s group by v."COD_SUCURSAL",v."FECHA" ) as ve on ve."COD_SUCURSAL"=s."ID"
	
group by s."ID",f.fecha_contable,f."Folio",ve.suma
order by s."ID" asc; ''',[fecha,fecha])
    ventas=v.objects.filter(fecha=fecha).aggregate(Sum('liquidacion'))
    
    
    context={'tablas':tablas, 'fecha':fecha,'ventas':ventas}
    return render(request,'facturas/revision_facturas_salida.html',context)    
def guias_vs_facturas(request):
    tiendas=s.objects.all()
    context={'sucursales':tiendas}
    
    return render(request,'facturas/guias_vs_facturas.html',context)
def guias_vs_facturas_salida(request,cod_suc):
    encuadre=gd.objects.raw(''' select 1 as unico,unico.isbn,l."TITULO" as titulo,unico.enviados,sum(v."VENTA") as vendidos,unico.enviados-sum(v."VENTA") as saldo from (select isbn,sum(cantidad)as enviados from guias_despacho gi where gi.cod_sucursal=%s group by isbn) as unico
left join ventas v on v."COD_SUCURSAL"=%s and unico.isbn=v."ISBN"
left join listadoinicial l on unico.isbn=l."ISBN"
group by unico.isbn,l."TITULO",unico.enviados
order by unico.isbn desc;   
 ''',[cod_suc,cod_suc] )
    ultimos_envios=gd.objects.filter(cod_sucursal=cod_suc).distinct('numero_guia_factura').order_by('-numero_guia_factura')
    sucursal=s.objects.filter(id=cod_suc)
    context={'encuadre':encuadre,'sucursal':sucursal,'ultimos_envios':ultimos_envios}
    
    return render(request,'facturas/guias_vs_factura_salida.html',context)
def actualizar_ventas(request):
    conn=psycopg2.connect("dbname=GA_db user=postgres")
    cur=conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    conn.close()
    return HttpResponseRedirect('/intra/')
    
def mas_vendidos(request):
    context={}
    context['tiendas']=s.objects.all()
    return render(request,'facturas/mas_vendidos.html',context)

def mas_vendidos_salida(request,cod_suc):
    mas_vendidos=v.objects.raw(''' select 1 as id_number, "ISBN" as isbn ,"DESCRIPCION" as descripcion ,sum("VENTA") as ventas 
from ventas v where "COD_SUCURSAL"=%s group by "COD_SUCURSAL","ISBN","DESCRIPCION" order by sum("VENTA") desc; ''',[cod_suc]) 
    
    context={'mas_vendidos':mas_vendidos,'sucursal':s.objects.filter(id=cod_suc)}
    return render(request,'facturas/mas_vendidos_salida.html',context)
    
def ubicacion_stock(request,isbn):
    ubicacion=arq.objects.filter(isbn=isbn)
    context={'ubicacion':ubicacion}
    return render(request,'facturas/ubicacion_stock.html',context)

def encuadre_espana_vista(request):
    from .models import Importaciones as i
    from .models import EliminadosReal as el
    from .models import Liquidaciones as li
    context={}
    context['impo']=impo=i.objects.raw(''' select 1 as id, sum(valor_total) as impo from importaciones ''').__getitem__(0).impo
    context['eliminados']=eliminados=el.objects.raw(''' select 1 as id, sum(precio_total) as precio from eliminados_real ''').__getitem__(0).precio
    liquidaciones=li.objects.all().aggregate(Sum('valor_total'))
    context['liquidaciones']=liquidaciones['valor_total__sum']
    context['tiendas']=tiendas=v.objects.raw(''' select 1 as id_number, sum("SALDO"*"PRECIO_ESPAÑA") as venta_precio from ventas where "FECHA"=(select max("FECHA") from ventas)''').__getitem__(0).venta_precio
    context['bodega_valorizada']=bodega_valorizada=v.objects.raw(''' select 1 as id_number, sum(s.stock*l."PRECIO_ESPAÑA") as valorizado from stock_bodega s join listadoinicial l on s._isbn=l."ISBN" where s.stock>0''').__getitem__(0).valorizado
    context['fecha']=li.objects.raw(''' select 1 as id, max(fecha) as fecha from liquidaciones ''').__getitem__(0).fecha
    saldo=float(impo)-(float(tiendas)+float(bodega_valorizada)+float(liquidaciones['valor_total__sum'])+float(eliminados))
    
    return render(request,'facturas/encuadre.html',context)

def facturas_all(request):
    context={}
    
    impagas = FacturacionRegistro.objects.filter(pagada=False,vencida=True,tipo_documento=33).order_by('-fecha_vencimiento')
    context['impagas']=impagas
    context['sumas']=FacturacionRegistro.objects.filter(pagada=False,vencida=True,tipo_documento=33).aggregate(Sum('monto_neto')) 
    for imp in impagas:
        context['ultima_actualizacion'] = imp.ultima_actualizacion
        break

    return render(request,'facturas/facturas_all.html',context)

from .forms import facturas_filtradas_modelform as fa

def facturas_filtradas(request):
    inicial=0
    if request.method=="POST":
        #print("esta es en filtradas",request.POST)
        pasadas=request.POST.copy()
        facturas=pasadas.pop('factura')
        context={}
        facturas_seleccionadas=[]
        context['sumas']=int(0)
        inicial=0
        for i in facturas:
            q=FacturacionRegistro.objects.get(folio=i)
            inicial=inicial+int(q.monto_total)
            context['sumas']=inicial
            facturas_seleccionadas.append(q)
        context['seleccionadas']=facturas_seleccionadas
        
    return render(request,'facturas/facturas_seleccionadas.html',context)

def facturas_actualizadas(request):
    if request.method=="POST":
        algo=request.POST.copy()
        folios = algo.getlist('folio')
        otros_comentarios = algo.getlist('otros_comentarios')
        fecha_pago = algo.getlist('fecha_pago')
        numero_de_items=len(folios)
        for i in range(0,numero_de_items):
            #dicc={}
            #dicc['folio']=folios[i]
            #dicc['otros_comentarios']=
            #dicc['fecha_pago']=
            print(folios[i])
            q=FacturacionRegistro.objects.get(folio=folios[i])
            q.otros_comentarios=otros_comentarios[i]
            q.fecha_pago=fecha_pago[i]
            q.pagada=True
            q.save()
    return HttpResponse("Actualización Correcta.")