from django.shortcuts import render, redirect
from .models import Lista_tareas
from .forms import TareasForm


def tarea(request):
    form = TareasForm()
    if request.method == 'POST':
        form = TareasForm(request.POST)
        if form.is_valid():
            tareas = form.save(commit=False)
            tareas.save()
            return redirect ('/')       
    return render(request, 'form.html', {'form': form})

def lista(request):
    tareas = Lista_tareas.objects.all() 
    return render(request, 'lista.html', {'Lista_tareas': tareas})
