from django.shortcuts import render

# Create your views here.
def Inicio(request):
    datos = {
        'bienvenida': 'Bienvenidos/as a Dent Corp'
    }

    return render(request, 'index.html', datos)