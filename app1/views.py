from django.shortcuts import render


# Create your views here.


def inicio(request):
    return render(request, 'app1/inicio.html')


def informacion(request):
    return render(request, 'app1/informacion.html')

# Create your views here.
