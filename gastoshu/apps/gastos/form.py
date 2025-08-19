from django import forms
from .models import Gasto

class GastoForm(forms.ModelForm):
    class Meta:
        model = Gasto
        fields = ['fecha', 'monto', 'categoria', 'descripcion']
