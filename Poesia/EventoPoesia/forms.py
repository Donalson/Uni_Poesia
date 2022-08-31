from dataclasses import field
from django.forms import ModelForm
from .models import Poesia

class Formulario_EventoPoesia(ModelForm):
    class Meta:
        model = Poesia
        fields = '__all__'
        #widgets = {}