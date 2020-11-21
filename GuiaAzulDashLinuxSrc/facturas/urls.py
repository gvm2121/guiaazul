from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('datos-grafico/<int:cod_suc>', views.datos, name='datos'),
    path('datos-grafico-historico/<int:cod_suc_2>', views.analisis_sucursal_historico, name='datos_2'),
    path('stock', views.vista_stock, name='vista_stock'),
    path('stock/ubicacion_stock/<str:isbn>', views.ubicacion_stock, name='ubicacion_stock'),
    path('analisis_sucursal', views.analisis_sucursal, name='analisis_sucursal'),
    path('analisis_titulo', views.analisis_titulo, name='analisis_titulo'),
    path('factura/exportar_facturas_impagas_csv', views.exportar_facturas_impagas_csv, name='exportar_facturas_impagas_csv'),
    path('stock/csv_stock', views.csv_stock, name='csv_stock'),
    path('analisis_sucursal/exportar_csv/<str:nombre_sucursal>', views.csv_sucursal, name='csv_sucursal'),
    path('historico', views.historico, name='historico'),
    path('busqueda', views.busqueda, name='busqueda'),
    path('busqueda_isbn', views.busqueda_isbn, name='busqueda_isbn'),
    path('tablaventas', views.tablaventas, name='tablaventas'),
    path('tablaventas/recibo', views.tablaventas_recibo, name='tablaventas_recibo'),
    path('stock/buscalibre', views.buscalibre_csv, name='buscalibre_csv'),
    path('analisis_sucursal/mas_vendidos', views.mas_vendidos, name='mas_vendidos'),
    path('analisis_sucursal/ratios', views.ratios, name='ratios'),
    path('analisis_sucursal/validador_facturas', views.validador_facturas, name='validador_facturas'),
    path('analisis_sucursal/facturas_all', views.facturas_all, name='facturas_all'),
    path('analisis_sucursal/facturas_recibo', views.facturas_filtradas, name='facturas_filtradas'),
    path('analisis_sucursal/facturas_actualizadas', views.facturas_actualizadas, name='facturas_actualizadas'),
    path('analisis_sucursal/validador_facturas_salida/<str:fecha>', views.validador_facturas_salida, name='validador_facturas_salida'),
    path('guias_vs_facturas', views.guias_vs_facturas, name='guias_vs_facturas'),
    path('guias_vs_facturas/<int:cod_suc>', views.guias_vs_facturas_salida, name='guias_vs_facturas_salida'),
    path('actualizar_ventas', views.actualizar_ventas, name='actualizar_ventas'),
    path('mas_vendidos', views.mas_vendidos, name='mas_vendidos'),
    path('mas_vendidos/<int:cod_suc>', views.mas_vendidos_salida, name='mas_vendidos_salida'),
    path('encuadre-espana', views.encuadre_espana_vista, name='encuadre_espana_vista'),
    
]