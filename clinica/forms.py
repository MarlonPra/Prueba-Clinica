from django import forms
from .models import Paciente, Municipio, Diagnostico, Historial
import datetime

class PacienteForm(forms.ModelForm):
    fecha_nacimiento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Paciente
        fields = ['nombre', 'apellido', 'fecha_nacimiento', 'municipio']

    def clean_fecha_nacimiento(self):
        fecha_nacimiento = self.cleaned_data.get('fecha_nacimiento')
        if fecha_nacimiento and fecha_nacimiento > datetime.date.today():
            raise forms.ValidationError("La fecha de nacimiento no puede ser futura.")
        return fecha_nacimiento

class MunicipioForm(forms.ModelForm):
    class Meta:
        model = Municipio
        fields = ['nombre', 'departamento']

class DiagnosticoForm(forms.ModelForm):
    class Meta:
        model = Diagnostico
        fields = ['codigo', 'nombre']

class HistorialForm(forms.ModelForm):
    class Meta:
        model = Historial
        fields = ['paciente', 'diagnostico', 'observaciones']