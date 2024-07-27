from django.urls import path
from . import views

urlpatterns = [
    path('', views.root, name='root'),
    path('home/', views.home, name='home'),  
    path('edit-user/', views.edit_user, name='edit_user'),  
    path('detalle/<int:pk>', views.detalle, name='detalle'),
    path('success/', views.success, name='success'),
]