from django.contrib.auth.models import User
from main.models import UserProfile, Inmueble, Comuna
from django.db.utils import IntegrityError
from django.db.models import Q
from django.db import connection

def crear_inmueble(nombre, descripcion, m2_construidos, m2_totales, n_estacionamientos, n_habitaciones, n_banos, direccion, tipo_inmueble, precio, comuna_cod, propietario_rut):
    comuna = Comuna.objects.get(cod=comuna_cod)
    propietario = User.objects.get(username=propietario_rut)
    Inmueble.objects.create(nombre=nombre, descripcion=descripcion, m2_construidos=m2_construidos, m2_totales=m2_totales, n_estacionamientos=n_estacionamientos, n_habitaciones=n_habitaciones, n_banos=n_banos, direccion=direccion, tipo_inmueble=tipo_inmueble, precio=precio, comuna_cod=comuna, propietario_rut=propietario)

def editar_inmueble(inmueble_id, nombre=None, descripcion=None, m2_construidos=None, m2_totales=None,n_estacionamientos=None, n_habitaciones=None, n_banos=None, direccion=None, tipo_inmueble=None, precio=None,comuna_cod=None):
    try:
        inmueble = Inmueble.objects.get(id=inmueble_id)
        if nombre is not None:
            inmueble.nombre = nombre
        if descripcion is not None:
            inmueble.descripcion = descripcion
        if m2_construidos is not None:
            inmueble.m2_construidos = m2_construidos
        if m2_totales is not None:
            inmueble.m2_totales = m2_totales
        if n_estacionamientos is not None:
            inmueble.n_estacionamientos = n_estacionamientos
        if n_habitaciones is not None:
            inmueble.n_habitaciones = n_habitaciones
        if n_banos is not None:
            inmueble.n_banos = n_banos
        if direccion is not None:
            inmueble.direccion = direccion
        if tipo_inmueble is not None:
            inmueble.tipo_inmueble = tipo_inmueble
        if precio is not None:
            inmueble.precio = precio
        if comuna_cod is not None:
            comuna = Comuna.objects.get(cod=comuna_cod)
            inmueble.comuna = comuna
        inmueble.save()
        return True
    except Inmueble.DoesNotExist:
        return False

def eliminar_inmueble(inmueble_id):
    try:
        inmueble = Inmueble.objects.get(id=inmueble_id)
        inmueble.delete()
        return True
    except Inmueble.DoesNotExist:
        return False

def crear_user(username, first_name, last_name, email, password, pass_confirm, direccion, telefono=None) -> list[bool, str]:
    #VALIDAR PASSWORD
    if password != pass_confirm:
        return False, 'Las contraseñas no coinciden'
    #CREAR USER
    try:
        user = User.objects.create_user(username,email, password,first_name=first_name, last_name=last_name)
    except IntegrityError:
        return False, 'RUT duplicado'
    #CREAR USERPROFILE
    UserProfile.objects.create(user=user,direccion=direccion, telefono=telefono)
    return True, None

def editar_user(username, first_name, last_name, email, password, pass_confirm, direccion, telefono=None) -> list[bool, str]:
    #EDICION DEL USER
    user = User.objects.get(username=username)
    user.first_name = first_name
    user.last_name = last_name
    user.email = email
    user.set_password(password)
    user.save()
    #EDICION DEL USERPROFILE
    user_profile = UserProfile.objects.get(user=user)
    user_profile.direccion = direccion
    user_profile.telefono = telefono
    user_profile.save()

def eliminar_user(user_id):
    try:
        user = User.objects.get(id=user_id)
        user.delete()
        return True
    except User.DoesNotExist:
        return False
    
def obtener_inmuebles_comunas(filtro):
    if filtro is None:
        return Inmueble.objects.all().order_by('comuna_cod')
    return Inmueble.objects.filter(Q(nombre__icontains=filtro) | Q(descripcion__icontains=filtro)).order_by('comuna_cod')