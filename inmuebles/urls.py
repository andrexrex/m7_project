from django.urls import path
from . import views

urlpatterns = [
    path('nuevo/', views.nuevo_inmueble, name='nuevo_inmueble'),  
    path('crear/', views.crear_inmueble, name='crear_inmueble'),  
    path('editar/<id>/', views.editar_inmueble, name='editar_inmueble'),  
    path('eliminar/<id>/', views.eliminar_inmueble, name='eliminar_inmueble')
]