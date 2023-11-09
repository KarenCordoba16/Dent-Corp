from django.shortcuts import render, redirect
from .models import Turno
from .forms import TurnoForm
from django.http import HttpResponse

def calendario_view(request):
    turnos = Turno.objects.all()
    return render(request, 'calendar/calendario.html', {'turnos': turnos})

def agregar_turno(request):
    if request.method == 'POST':
        form = TurnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('calendario')
    else:
        form = TurnoForm()
    return render(request, 'calendar/agregar_turno.html', {'form': form})

def home(request):
    return HttpResponse('<h1>¡Bienvenid@!</h1>')

