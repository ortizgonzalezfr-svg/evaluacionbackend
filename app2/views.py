from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'app2/index.html')


def contacto(request):
    return render(request, 'app2/contacto.html')