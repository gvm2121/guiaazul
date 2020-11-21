from django.db import models




class FacturacionRegistro(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)  # Field name made lowercase.
    folio = models.IntegerField(db_column='Folio')  # Field name made lowercase.
    rut = models.TextField(db_column='Rut')  # Field name made lowercase.
    dirección = models.TextField(db_column='Dirección')  # Field name made lowercase.
    comuna = models.TextField(db_column='Comuna')  # Field name made lowercase.
    comentario = models.TextField(db_column='Comentario', blank=True, null=True)  # Field name made lowercase.
    monto_neto = models.TextField(db_column='Monto_neto')  # Field name made lowercase. This field type is a guess.
    iva = models.TextField(db_column='IVA')  # Field name made lowercase. This field type is a guess.
    monto_total = models.TextField(db_column='Monto_total')  # Field name made lowercase. This field type is a guess.
    fecha_emision = models.DateField(db_column='Fecha_emision')  # Field name made lowercase.
    vencida = models.NullBooleanField(db_column='Vencida')  # Field name made lowercase.
    cod_sucursal = models.IntegerField(db_column='Cod_sucursal', blank=True, null=True)  # Field name made lowercase.
    monto_españa = models.TextField(db_column='Monto_españa', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    monto_españa_pesos = models.TextField(db_column='Monto_españa_pesos', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    utilidad = models.TextField(db_column='Utilidad', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fecha_pago = models.DateField(db_column='Fecha_pago', blank=True, null=True)  # Field name made lowercase.
    pagada = models.NullBooleanField(db_column='Pagada')  # Field name made lowercase.
    otros_comentarios = models.TextField(blank=True, null=True)
    contenido = models.TextField(blank=True, null=True)
    mes_liq = models.IntegerField(blank=True, null=True)
    año_liq = models.IntegerField(db_column='AÑO_LIQ', blank=True, null=True)  # Field name made lowercase.
    fecha_vencimiento = models.DateField(db_column='FECHA_VENCIMIENTO', blank=True, null=True)  # Field name made lowercase.
    tipo_documento = models.IntegerField(blank=True, null=True)
    mes_string = models.TextField(blank=True, null=True)
    fecha_contable = models.DateField(blank=True, null=True)
    ultima_actualizacion = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = True
        db_table = 'facturacion_registro'

        



class Ventas(models.Model):
    isbn = models.TextField(db_column='ISBN', blank=True, null=True)  # Field name made lowercase.
    descripcion = models.TextField(db_column='DESCRIPCION', blank=True, null=True)  # Field name made lowercase.
    inicial = models.IntegerField(db_column='INICIAL',blank=True, null=True)  # Field name made lowercase.
    venta = models.IntegerField(db_column='VENTA',blank=True, null=True)  # Field name made lowercase.
    devol = models.IntegerField(db_column='DEVOL',  blank=True, null=True)  # Field name made lowercase.
    recep = models.IntegerField(db_column='RECEP', blank=True, null=True)  # Field name made lowercase.
    saldo = models.IntegerField(db_column='SALDO', blank=True, null=True)  # Field name made lowercase.
    costo = models.IntegerField(db_column='COSTO', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    liquidacion = models.TextField(db_column='LIQUIDACION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sucursal = models.TextField(db_column='SUCURSAL', blank=True, null=True)  # Field name made lowercase.
    mes = models.TextField(db_column='MES', blank=True, null=True)  # Field name made lowercase.
    año = models.IntegerField(db_column='AÑO', blank=True, null=True)  # Field name made lowercase.
    cadena = models.TextField(db_column='CADENA', blank=True, null=True)  # Field name made lowercase.
    precio_españa = models.TextField(db_column='PRECIO_ESPAÑA', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    total_españa = models.TextField(db_column='TOTAL_ESPAÑA', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pvp = models.TextField(db_column='PVP', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    total_pvp = models.TextField(db_column='TOTAL_PVP', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    euro = models.TextField(db_column='EURO', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    utilidad = models.IntegerField(db_column='UTILIDAD', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cod_sucursal = models.IntegerField(db_column='COD_SUCURSAL', blank=True, null=True)  # Field name made lowercase.
    cod_mes = models.IntegerField(db_column='cod_mes', blank=True, null=True)
    fecha = models.DateField(db_column='FECHA', blank=True, null=True)  # Field name made lowercase.
    rut = models.TextField(db_column='RUT', blank=True, null=True)  # Field name made lowercase.
    direccion = models.TextField(db_column='DIRECCION', blank=True, null=True)  # Field name made lowercase.
    comuna = models.TextField(db_column='COMUNA', blank=True, null=True)  # Field name made lowercase.
    id = models.IntegerField(db_column='ID',  blank=True, null=True)  # Field name made lowercase.
    id_unico = models.TextField(blank=True, null=True)
    id_number = models.BigAutoField(primary_key=True)
    class Meta:
        managed = False
        db_table = 'ventas'


class Clientes(models.Model):
    rut = models.TextField(db_column='RUT', blank=True, null=True)  # Field name made lowercase.
    dias = models.DecimalField(db_column='Dias', max_digits=1000, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'clientes'
    


        
class Sucursales(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nombre = models.TextField(db_column='NOMBRE')  # Field name made lowercase.
    rut = models.TextField(db_column='RUT', blank=True, null=True)  # Field name made lowercase.
    direccion = models.TextField(db_column='DIRECCION', blank=True, null=True)  # Field name made lowercase.
    comuna = models.TextField(db_column='COMUNA', blank=True, null=True)  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'sucursales'


class Vencimientos(models.Model):
    rut = models.TextField(db_column='RUT', blank=True, null=True)  # Field name made lowercase.
    dias = models.IntegerField(db_column='DIAS', blank=True, null=True)  # Field name made lowercase.

        
class StockBodega(models.Model):
    field_isbn = models.TextField(db_column='_isbn', blank=True, null=True)  # Field renamed because it started with '_'.
    field_titulo = models.TextField(db_column='_titulo', blank=True, null=True)  # Field renamed because it started with '_'.
    field_edicion = models.TextField(db_column='_edicion', blank=True, null=True)  # Field renamed because it started with '_'.
    inventario = models.IntegerField(blank=True, null=True)
    entrada = models.IntegerField(blank=True, null=True)
    salida = models.IntegerField(blank=True, null=True)
    stock = models.IntegerField(blank=True, null=True)
    id = models.IntegerField(primary_key=True )
    cod_fch = models.TextField(blank=True, null=True)
    bosa = models.TextField(blank=True, null=True)
    ultima_actualizacion = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'stock_bodega'


class FaltantesTabla(models.Model):
    isbn = models.TextField(blank=True, null=True)
    bosa = models.TextField(blank=True, null=True)
    nombre = models.TextField(blank=True, null=True)
    edicion = models.TextField(blank=True, null=True)
    costo_tienda = models.TextField(blank=True, null=True)  # This field type is a guess.
    tienda = models.IntegerField(primary_key=True)
    tienda_nombre = models.TextField(blank=True, null=True)
    fecha_contable = models.DateField(blank=True, null=True)
    saldo_bodega = models.DecimalField(max_digits=1000, decimal_places=2, blank=True, null=True)
    class Meta:
        managed = True
        db_table = 'faltantes_tabla'

        
class MovimientosBodega(models.Model):
    isbn = models.TextField()
    cantidad = models.SmallIntegerField()
    destino = models.TextField()
    motivo = models.TextField(blank=True, null=True)
    salida_ingreso = models.TextField()
    guia_factura = models.TextField(blank=True, null=True)
    numero_guia_factura = models.TextField(blank=True, null=True)
    odc = models.TextField(blank=True, null=True)
    comentarios = models.TextField(blank=True, null=True)
    tag = models.TextField(blank=True, null=True)
    cod_sucursal = models.IntegerField( blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    unico = models.AutoField(primary_key=True )
    class Meta:
        managed = True
        db_table = 'movimientos_bodega'

class VentasContrapuntoPilgrim(models.Model):
    id_unico=models.AutoField(primary_key=True)
    isbn = models.TextField(blank=True)
    venta = models.IntegerField( blank=True, null=True)
    cod_sucursal = models.IntegerField( blank=True, null=True)
    fecha_contable = models.DateField(blank=True, null=True)

        
class Listadoinicial(models.Model):
    id = models.DecimalField(max_digits=100, decimal_places=0)
    isbn = models.TextField(db_column='ISBN', primary_key=True)  # Field name made lowercase.
    titulo = models.TextField(db_column='TITULO', blank=True, null=True)  # Field name made lowercase.
    edicion = models.TextField(db_column='EDICION', blank=True, null=True)  # Field name made lowercase.
    pvp = models.TextField(db_column='PVP', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    precio_españa = models.TextField(db_column='PRECIO_ESPAÑA', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    precio_españa2 = models.TextField(db_column='PRECIO_ESPAÑA2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    rendir_españa = models.CharField(db_column='RENDIR_ESPAÑA', blank=True, null=True, max_length=3)  # Field name made lowercase.
    costo_tienda = models.TextField(blank=True, null=True)  # This field type is a guess.
    activo = models.NullBooleanField()
    bosa = models.TextField(blank=True, null=True)
    cod_feria = models.TextField(blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'listadoinicial'



class TablaCantidadTienda(models.Model):
    sucursal = models.DecimalField(max_digits=2, decimal_places=0,primary_key=True)
    nombre_sucursal = models.TextField(blank=True, null=True)
    venta = models.DecimalField(max_digits=4,decimal_places=0, blank=True, null=True)
    saldo = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'tabla_cantidad_tienda'


class GuiasDespacho(models.Model):
    isbn = models.TextField(blank=True, null=True)
    cantidad = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    destino = models.TextField(blank=True, null=True)
    motivo = models.TextField(blank=True, null=True)
    salida_ingreso = models.TextField(blank=True, null=True)
    guia_factura = models.TextField(blank=True, null=True)
    numero_guia_factura = models.TextField(blank=True, null=True)
    odc = models.TextField(blank=True, null=True)
    comentarios = models.TextField(blank=True, null=True)
    tag = models.TextField(blank=True, null=True)
    cod_sucursal = models.DecimalField(max_digits=1000, decimal_places=2, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    fecha_subida = models.DateField(blank=True, null=True)
    unico = models.AutoField(primary_key=True)
    id_unico = models.TextField(blank=True, null=True)
    nombre_item = models.TextField(blank=True, null=True)
    precio_item = models.TextField(blank=True, null=True)  # This field type is a guess.
    monto_item = models.TextField(blank=True, null=True)  # This field type is a guess.
    nombre_listado_inicial = models.TextField(blank=True, null=True)

class ArqueoOct2018(models.Model):
    isbn = models.TextField(blank=True, null=True)
    cantidad = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    ubicacion = models.TextField(blank=True, null=True)
    titulo = models.TextField(blank=True, null=True)
    edicion = models.TextField(blank=True, null=True)
    id=models.IntegerField(primary_key=True)
    class Meta:
        managed = True
        db_table = 'arqueo_oct_2018'

class Importaciones(models.Model):
    id = models.AutoField(primary_key=True)
    cantidad = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    valor_total = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    comentarios = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'importaciones'
        
class EliminadosReal(models.Model):
    isbn = models.TextField(blank=True, null=True)
    nombre = models.TextField(blank=True, null=True)
    cantidad = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    precio_unitario = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    precio_total = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    tag = models.TextField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'eliminados_real'

class Liquidaciones(models.Model):
    isbn = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    cantidad = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    valor_unitario = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True)
    valor_total = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    edicion = models.TextField(blank=True, null=True)
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'liquidaciones'



# Create your models here.
