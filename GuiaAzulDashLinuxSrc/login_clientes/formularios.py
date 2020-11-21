from django.forms import ModelForm,Textarea,TextInput,PasswordInput,EmailInput
from django import forms
from .models import ClienteModel

class login_cliente(forms.Form):
    correo=forms.CharField(label='correo', max_length=100)
    password=forms.CharField(label='password', max_length=100)

class cliente_nuevo_form(ModelForm):
    class Meta:
        model=ClienteModel
        fields='__all__'
        widgets={
            'rut':TextInput(attrs={'class':"form-control"}),
            'password':PasswordInput(attrs={'class':"form-control"}),
            'nombre':TextInput(attrs={'class':"form-control"}),
            'correo':EmailInput(attrs={'class':"form-control"}),
            'comuna_despacho':TextInput(attrs={'class':"form-control"}),
            'direccion_envio':Textarea(attrs={'class':"form-control"}),
            
        }
   
