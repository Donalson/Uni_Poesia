from django.shortcuts import redirect, render, HttpResponse
from django.contrib import messages

# Funcion de vista para mostrar el formulario de inicio de sesion
def login(request):

    #Si la peticion viene con metodo post ejecutar este codigo
    if request.method == 'POST':
        #Obtenemos los datos entrantes del formulario
        user = request.POST['username']
        password = request.POST['password']

        #Aqui deberi ir la logica para verificar el login en la api 
        ############################################################
        usuarios = ['Donalson', 'Jacobo', 'Admin', 'Prueba']
        contraseñas = ['1517', '3840', '1234', '4321']
        #En caso de que la informacion sea la necesario
        if(user in usuarios and password in contraseñas):
            #Codigo si conincide la informacion
            #respuesta = 'Sesion iniciada, Bienvenido: {}'.format(user)
            #return HttpResponse(respuesta)
            return redirect('/')
        #En caso contrario
        else:
            messages.error(request, 'Usuario o contraseña incorrecta')
            return render(request, 'Login/login.html', {})
    #Si la peticion no es de tipo POST
    else:
        return render(request, 'Login/login.html', {})

    return HttpResponse('URL por si se necesita registrar usuarios')