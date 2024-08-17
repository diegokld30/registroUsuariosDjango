from django.shortcuts import render, redirect
from .models import Persona
from .form import PersonaForm

# Create your views here.

def registerUser(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registerUser')
    else:
        form = PersonaForm()

    return render(request, 'registerUser.html', )

