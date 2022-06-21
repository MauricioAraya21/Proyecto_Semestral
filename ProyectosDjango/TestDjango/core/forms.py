from dataclasses import fields
from django import forms
from .models import formulario


class formularioForm(forms.ModelForm):
    

    class Meta:
        model = formulario
        fields = '__all__'