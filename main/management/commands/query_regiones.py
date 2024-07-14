import csv
from django.core.management.base import BaseCommand
from main.services import obtener_inmuebles_region

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('-f', '--f', type=str, nargs='+',)

    def handle(self, *args, **kwargs):
        filtro = None
        if 'f' in kwargs.keys() and kwargs['f'] is not None:
            filtro = kwargs['f'][0]

        inmuebles = obtener_inmuebles_region(filtro)
        registros = []
        for inmueble in inmuebles:
            linea = f'{inmueble.nombre}\t{inmueble.descripcion}\t{inmueble.comuna.region.nombre}'
            print(linea)
            registros.append(linea)
            
        with open('data/inmuebles_region.txt', 'w', encoding='utf-8') as f:
            for line in registros:
                f.write(line + '\n')