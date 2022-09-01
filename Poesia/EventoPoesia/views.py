from business_calendar import Calendar, MO, TU, WE, TH, FR
from pandas.tseries.offsets import BMonthEnd
from datetime import datetime
from dateutil.relativedelta import relativedelta
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Poesia

# Create your views here.
@login_required(login_url='Login', redirect_field_name='luego')
def formulario_registro(request):
    if request.method == 'POST':
        Carnet = request.POST['Carnet']
        if ValidarCarnet(Carnet):

            NombreCompleto = request.POST['NombreCompleto']
            Direccion = request.POST['Direccion']
            Genero = request.POST['Genero']
            Telefono = request.POST['Telefono']
            FNacimiento = request.POST['FNacimiento']
            if ValidarEdad(FNacimiento):

                Carrera = request.POST['Carrera']
                GeneroPoesia = request.POST['GeneroPoesia']
                FInscripcion = request.POST['FInscripcion']
                FDeclamacion = FechaDeclamacion(Carnet[5], FInscripcion, GeneroPoesia)
                #datos = f'Carnet="{Carnet}", Nombre_Completo="{NombreCompleto}", Direccion="{Direccion}", Genero="{Genero}", Telefono="{Telefono}", Fecha_Nacimiento="{FNacimiento}", Carrera_Estudiante="{Carrera}", Genero_Poesia="{GeneroPoesia}", Fecha_Declamacion="{FDeclamacion}"'
                #print(datos)
                #Registro = Poesia.objects.create(Carnet=f"{Carnet}", Nombre_Completo=f"{NombreCompleto}", Direccion=f"{Direccion}", Genero=f"{Genero}", Telefono=f"{Telefono}", Fecha_Nacimiento=f"{FNacimiento}", Carrera_Estudiante=f"{Carrera}", Genero_Poesia=f"{GeneroPoesia}", Fecha_Declamacion=f"{FDeclamacion}")
                #Registro = Poesia(Carnet=str(Carnet), Nombre_Completo=str(NombreCompleto), Direccion=str(Direccion), Genero=str(Genero), Telefono=str(Telefono), Fecha_Nacimiento=FNacimiento, Carrera_Estudiante=str(Carrera), Genero_Poesia=str(GeneroPoesia), Fecha_Declamacion=FDeclamacion)
                #print(type(FNacimiento))
                Registro = Poesia(Carnet=f'{Carnet}', Nombre_Completo=f'{NombreCompleto}', Direccion=f'{Direccion}', Genero=f'{Genero}', Telefono=f'{Telefono}', Fecha_Nacimiento='2000-09-26', Carrera_Estudiante=f'{Carrera}', Genero_Poesia=f'{GeneroPoesia}', Fecha_Declamacion='2022-08-31')
                """
                if Registro.save():
                    messages.success(request, f'Se registrado exitosamente {NombreCompleto}, su fecha de declamacion es: {FDeclamacion}')
                    return redirect('Formulario_Registro')
                else: 
                    messages.error(request, 'Parece que algo salio mal')
                    return redirect('Formulario_Registro')
                """
                return redirect('Formulario_Registro')
            else:
                messages.warning(request, 'Debe ser mayor de 17 años para participar')
                return redirect('Formulario_Registro')
        else:
            messages.warning(request, 'El carnet no es valido, el primer caracter debe ser "A", el terrcero "5", el ultimo "1/3/9" y no se permiten "0"')
            return redirect('Formulario_Registro')
    else: 
        return render(request, 'EventoPoesia/formulario_registro.html')

@login_required(login_url='Login', redirect_field_name='luego')
def reportes_poesia(request):
    datos = Poesia.objects.all()
    context = {'Registros':datos}
    return render(request, 'EventoPoesia/reportes_poesia.html', context)

def ValidarCarnet(Carnet):
    Validacion = True
    if Carnet[0] != 'A' and Carnet[2] != '5':
        Validacion = False
    if Carnet[5] != '1' and Carnet[5] != '3' and Carnet[5] != '9':
        Validacion = False
    if '0' in Carnet:
        Validacion = False
    return Validacion

def ValidarEdad(FN):
    FNacimiento = datetime.strptime(FN, '%Y-%m-%d')
    edad = relativedelta(datetime.now(), FNacimiento)
    if edad.years > 17:
        return True
    else:
        return False

def FechaDeclamacion(CA, FI, GP):
    cal = Calendar()

    if CA == '1' and GP == 'D':
        FD = str(cal.addbusdays(FI, 5))
        return FD[0:10]
    elif CA == '3' and GP == 'E':
        offset = BMonthEnd()
        FD = str(offset.rollforward(FI))
        return FD[0:10]
    else:
        date = datetime.strptime(FI, '%Y-%m-%d').isocalendar()
        friday = datetime.fromisocalendar(date[0], date[1], 5)
        return str(friday)[0:10]
