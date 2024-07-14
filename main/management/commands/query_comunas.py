from django.core.management.base import BaseCommand
import csv
from main.services import obtener_inmuebles_comunas

#python manage.pY test_client
class Command(BaseCommand):
    def add_arguments(self, parser):
    # Positional arguments
        parser.add_argument('-f', '--f', type=str, nargs='+',)

    def handle(self, *args, **kwargs):
        filtro = None
        if 'f' in kwargs.keys() and kwargs['f'] is not None:
            filtro = kwargs['f'][0]
        inmuebles = obtener_inmuebles_comunas(filtro)
        for inmueble in inmuebles:
            linea = f'{inmueble.nombre}\t{inmueble.descripcion}\t{inmueble.comuna_cod.nombre}'
            print(linea)