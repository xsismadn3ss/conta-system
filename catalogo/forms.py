from django import forms
from .models import Jerarquia, Tipo, Cuenta

class JerarquiaForm(forms.ModelForm):
    class Meta:
        model = Jerarquia
        fields = ["nombre"]

class TipoForm(forms.ModelForm):
    class Meta:
        model = Tipo
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'})
        }

class CuentaForm(forms.ModelForm):
    class Meta:
        model = Cuenta
        fields = ['nombre', 'tipo', 'jerarquia', 'estado']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'jerarquia': forms.Select(attrs={'class': 'form-control'}),
            'estado': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }