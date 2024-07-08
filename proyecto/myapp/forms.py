# forms.py
from django import forms
from .models import ProduccionDiaria

class ProduccionDiariaForm(forms.ModelForm):
    class Meta:
        model = ProduccionDiaria
        fields = ['estacion', 'fecha', 'litrosProduccion', 'codigoCombustible','hora','turno','codigoPlanta']
