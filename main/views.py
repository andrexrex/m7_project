from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from main.forms import RegisterUserForm
from main.services import editar_user_sin_password

class CustomLoginView(SuccessMessageMixin, LoginView):
    success_message = "Sesion Iniciada Exitosamente"
    template_name = 'registration/login.html'  
    redirect_authenticated_user = True
    
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('home')
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.add_message(request, messages.WARNING, "Sesion Cerrada Exitosamente")
        return response

def root(request):
    return redirect('/home')

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def profile(req):
    return render(req, 'profile.html')

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
            req.POST['telefono'])
    else:
        editar_user_sin_password(
            current_user.username,
            req.POST['first_name'],
            req.POST['last_name'],
            req.POST['email'],
            req.POST['direccion'])
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

