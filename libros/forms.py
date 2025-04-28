from django import forms
from .models import LibroMayor, Tipo

class LibroMayorForm(forms.ModelForm):
    class Meta:
        model = LibroMayor
        fields = ['saldo_anterior', 'movimiento', 'saldo_final', 'tipo_movimiento', 'cuenta']
        widgets = {
            'saldo_anterior': forms.NumberInput(attrs={'class': 'form-control'}),
            'movimiento': forms.NumberInput(attrs={'class': 'form-control'}),
            'saldo_final': forms.NumberInput(attrs={'class': 'form-control'}),
            'tipo_movimiento': forms.Select(attrs={'class': 'form-control'}),
            'cuenta': forms.Select(attrs={'class': 'form-control'})
        }

class TipoForm(forms.ModelForm):
    class Meta:
        model = Tipo
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el nombre del tipo'
            })
        }
        error_messages = {
            'nombre': {
                'unique': 'Este nombre ya existe',
                'required': 'Este campo es obligatorio'
            }
        }