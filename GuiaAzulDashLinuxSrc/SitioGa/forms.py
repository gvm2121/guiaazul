from django import forms

class FormularioContacto(forms.Form):
	Nombre=forms.CharField(widget=forms.TextInput(attrs={'style':'width:100%;height:35px;'}))
	Email=forms.EmailField(widget=forms.TextInput(attrs={'style':'width:100%;height:35px;'}))
	Pais=forms.CharField(widget=forms.TextInput(attrs={'style':'width:100%;height:35px;'}))
	Mensaje=forms.CharField(widget=forms.TextInput(attrs={'style':'width:100%;height:150px;'}))

