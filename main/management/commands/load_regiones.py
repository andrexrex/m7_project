from django.core.management.base import BaseCommand
import csv
from main.models import Region

#python manage.pY test_client
class Command(BaseCommand):
    def handle(self,*args,**kwargs):
        archivo = open('data/comunas.csv', encoding='utf-8')
        reader = csv.reader(archivo, delimiter=';')
        next(reader)
        nombres_regiones = []
        for fila in reader:
            if fila[2] not in nombres_regiones:
                Region.objects.create(nombre=fila[2],cod=fila[3])
                nombres_regiones.append(fila[2])
        print(nombres_regiones)