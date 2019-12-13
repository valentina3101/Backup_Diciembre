from django.db import models

class Lista_tareas(models.Model):
    tarea = models.CharField(max_length =100)
    realizada =models.BooleanField(default=False)

