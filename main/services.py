from django.contrib.auth.models import User
from main.models import UserProfile
from django.db.utils import IntegrityError

def crear_inmueble(*args):
    pass
def editar_inmueble(*args):
    pass
def eliminar_inmueble(inmueble_id):
    pass

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
    pass

