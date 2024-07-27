from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from main.models import Comuna, Inmueble, Region
from main.forms import RegisterUserForm
from django.db.models import Q
from main.services import editar_user_sin_password

class CustomLoginView(SuccessMessageMixin, LoginView):
    success_message = "Sesion Iniciada Exitosamente"
    template_name = 'registration/login.html'  
    redirect_authenticated_user = True

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('home')

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        
        # Clear messages
        storage = messages.get_messages(request)
        list(storage)  # Consume the generator to clear the messages
        
        # Add a single message
        messages.add_message(request, messages.WARNING, "Sesion Cerrada Exitosamente")
        
        return response
    
def root(request):
    return redirect('/home')

@login_required
def home(request):
    datos = request.GET
    region_cod = datos.get('region_cod', '')
    comuna_cod = datos.get('comuna_cod', '')
    palabra = datos.get('palabra', '')

    regiones = Region.objects.all()
    comunas = Comuna.objects.all()
    inmuebles = filtrar_inmuebles(region_cod, comuna_cod, palabra)
    info = generar_info(region_cod, comuna_cod, palabra)

    context = {
        'regiones': regiones,
        'comunas': comunas,
        'inmuebles': inmuebles,
        'info': info,
    }
    return render(request, 'home.html', context)

def filtrar_inmuebles(region_cod, comuna_cod, palabra):
    inmuebles = Inmueble.objects.all()
    if comuna_cod:
        inmuebles = inmuebles.filter(comuna__cod=comuna_cod)
    elif region_cod:
        inmuebles = inmuebles.filter(comuna__region__cod=region_cod)
    if palabra:
        inmuebles = inmuebles.filter(
            Q(nombre__icontains=palabra) | Q(descripcion__icontains=palabra)
        )
    return inmuebles

def generar_info(region_cod, comuna_cod, palabra):
    info = ""
    if region_cod:
        region = Region.objects.get(cod=region_cod)
        info += f"En Región {region.nombre}"
    if comuna_cod:
        comuna = Comuna.objects.get(cod=comuna_cod)
        if info:
            info += ", "
        info += f"{comuna.nombre}"
    if palabra:
        if info:
            info += ", "
        info += f"con '{palabra}'"
    return info

@login_required
def profile(req):
    user = req.user
    mis_inmuebles = None
    if user.user_profile.rol == 'arrendador':
        mis_inmuebles = user.inmuebles.all()
    elif user.user_profile.rol == 'arrendatario':
        pass
    context = {
        'mis_inmuebles': mis_inmuebles
    }
    return render(req, 'profile.html', context)

@login_required
def edit_user(req):
    # 1. Obtengo el usuario actual
    current_user = req.user
    # llamo a la función para editar el usuario
    if req.POST['telefono'] != '':
        # trailing whitespaces .strip()
        editar_user_sin_password(
            current_user.username,
            req.POST['first_name'],
            req.POST['last_name'],
            req.POST['email'],
            req.POST['direccion'],
            req.POST['rol'],
            req.POST['telefono'])
    else:
        editar_user_sin_password(
            current_user.username,
            req.POST['first_name'],
            req.POST['last_name'],
            req.POST['email'],
            req.POST['direccion'],
            req.POST['rol'])
    messages.success(req, "Ha actualizado sus datos con éxito")
    return redirect('/')

def change_password(req):
    # 1. Recibo los datos del formulario
    password = req.POST['password']
    pass_repeat = req.POST['pass_repeat']
    # 2. Valido que ambas contraseñas coincidan
    if password != pass_repeat:
        messages.error(req, 'Las contraseñas no coinciden')
        return redirect('/accounts/profile')
    # 3. Actualizamos la contraseña
    req.user.set_password(password)
    req.user.save()
    # 4. Le avisamos al usuario que el cambio fué exitoso
    messages.success(req, 'Contraseña actualizada')
    return redirect('/accounts/profile')

def solo_arrendadores(request):
    return HttpResponse('solo arrendadores')

def solo_arrendatarios(request):
    return HttpResponse('solo arrendatarios')

def success(request):
    return render(request,'success.html')    

def detalle(request, pk):
    inmueble = get_object_or_404(Inmueble, pk=pk)
    return render(request, 'detalle.html', {'inmueble': inmueble})

