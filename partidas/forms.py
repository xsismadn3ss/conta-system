from django import forms
from .models import PartidaRegistro, Detalles

class PartidaForm(forms.ModelForm):
    class Meta:
        model = PartidaRegistro
        fields = ['titulo', 'descripcion']
        widgets = {
            'fecha_creacion': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class DetallesForm(forms.ModelForm):
    class Meta:
        model = Detalles
        fields = ['monto_debe', 'monto_haber', 'partida', 'catalogo_cuentas']