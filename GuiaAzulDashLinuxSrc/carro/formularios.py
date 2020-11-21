from django import forms

class formulariocantidad(forms.Form):
    cantidad=forms.IntegerField(min_value=1, max_value=5)