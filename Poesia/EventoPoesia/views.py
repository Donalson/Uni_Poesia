from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Poesia

# Create your views here.
@login_required(login_url='Login', redirect_field_name='luego')
def formulario_registro(request):
    return render(request, 'EventoPoesia/formulario_registro.html', {})

@login_required(login_url='Login', redirect_field_name='luego')
def reportes_poesia(request):
    return render(request, 'EventoPoesia/reportes_poesia.html', {})