import psycopg2 as p


conn2=p.connect("dbname=ga_respaldo user=postgres password=gonzalovera26 host=localhost")
print("conectado a GA_RESPALDO")
cur3=conn2.cursor()
cur3.execute('''update facturacion_registro set "Vencida"=false; update facturacion_registro set "Vencida"=true where CURRENT_DATE>"FECHA_VENCIMIENTO";update facturacion_registro set ultima_actualizacion=current_timestamp;Update facturacion_registro f set "Comentario"='' where f."Comentario" is null;Update facturacion_registro f set "Pagada"=false where f."Pagada" is null;''')
conn2.commit()
cur3.execute('insert into stock_bodega_historico select * from stock_bodega;delete from stock_bodega;insert into stock_bodega select * from stock();update stock_bodega bo set cod_fch=(select l.cod_feria from listadoinicial l where bo._isbn=l."ISBN");update stock_bodega bo set bosa=(select l.bosa from listadoinicial l where bo._isbn=l."ISBN");update stock_bodega bo set ultima_actualizacion=current_timestamp;')
conn2.commit()
conn2.close()
print("Cerrado GA_RESPALDO")



