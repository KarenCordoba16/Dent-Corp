from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required

def Inicio(request):
    datos = {
        'bienvenida': 'Bienvenidos/as a Dent Corp'
    }

    return render(request, 'base.html', datos)

def register(request):
    if request.method == 'GET':
        return render(request, 'registration/register.html', {'form': CustomUserCreationForm})
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)

        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            user = authenticate(
                email = form.cleaned_data['email'],
                password = form.cleaned_data['password']
            )
            login(request, user)

            return redirect('home')
        else:
            return render(request, 'registration/register.html', {"form":form})
        
@login_required
def home(request):
    context = {}

    return render(request, 'home/index.html', context)