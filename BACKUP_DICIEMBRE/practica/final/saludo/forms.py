from django.forms import ModelForm
from .models import Lista_tareas


class TareasForm(ModelForm):
    class Meta:
        model = Lista_tareas
        fields = ['tarea', 'realizada']
