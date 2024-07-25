from django.forms import ModelForm
from main.models import Inmueble
from django import forms

class InmuebleForm(ModelForm):
    class Meta:
        model = Inmueble
        exclude = []
        widgets = {
        'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
        'm2_construidos': forms.NumberInput(attrs={'class': 'form-control'}),
        ## Completar el resto de los campos
        }