from django.core.management.base import BaseCommand
import csv
from main.services import crear_inmueble

#python manage.pY test_client
class Command(BaseCommand):
    def handle(self,*args,**kwargs):
        archivo = open('data/inmuebles.csv', encoding='utf-8')
        reader = csv.reader(archivo, delimiter=';')
        next(reader)
        for fila in reader:
            crear_inmueble(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5], fila[6], fila[7], fila[8], fila[9], fila[10], fila[11], fila[12], fila[13], fila[14], fila[15])
