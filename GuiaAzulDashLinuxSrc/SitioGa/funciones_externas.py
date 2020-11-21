from .models import SitiogaWeb as web
from facturas.models import StockBodega as saldo
import os, fnmatch,re
BASE_DIR2=os.path.join(os.getcwd(),'static','SitioGa','imagenes')

class libro_objeto:
    def __init__(self,isbn):
        self.isbn=isbn  
        self.nombre=web.objects.get(libro__isbn__icontains=self.isbn).libro.titulo
        stk=saldo.objects.get(field_isbn__icontains=isbn).stock
        self.pvp=web.objects.get(libro__isbn__icontains=self.isbn).libro.pvp
        self.contenido='este es el contenido'
        if stk>6:
            self.stock='Disponible'
        else:
            self.stock='No Disponible'
        self.foto=0
        dic={'GUIA AZUL':'','ED':'',' ':'','-':''}
        texto=self.nombre
        for i,j in dic.items():
            texto=texto.replace(i,j)

        texto=texto.strip()
        texto=re.search('[\D]+',texto).group()
        
                
        for f in os.listdir(BASE_DIR2):
            if fnmatch.fnmatch(f,'*'+texto+'*.jpg') or fnmatch.fnmatch(f,'*'+texto.lower()+'*.jpg') or fnmatch.fnmatch(f,'*'+texto.upper()+'*.jpg') or fnmatch.fnmatch(f,'*'+self.isbn+'*.jpg'):
                self.foto=f
                break
            else:
                self.foto=0
            
