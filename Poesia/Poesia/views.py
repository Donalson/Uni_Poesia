from django.shortcuts import render

def index(request):
    return render(request, 'Poesia/index.html', {})

def reportes_poesia(request):
    return render(request, 'Poesia/reportes.html', {})