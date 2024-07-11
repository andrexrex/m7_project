from django.core.management.base import BaseCommand
from main.services import *

#python manage.pY test_client
class Command(BaseCommand):
    def handle(self,*args,**kwargs):
        crear_user(
            '1234567-8',
            'Pedro',
            'Picapiedras',
            'picapiedra@gmail.com',
            '12345',
            '12345',
            'Av. Roca 455'
        )