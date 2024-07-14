from django.urls import path
from . import views

urlpatterns = [
    path('', views.root, name='root'),
    path('index/', views.index, name='index'),
    path('register/', views.register, name='register'),
]