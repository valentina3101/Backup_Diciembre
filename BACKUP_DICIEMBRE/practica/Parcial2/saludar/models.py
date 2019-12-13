
from django.db import models
from django.forms import ModelForm


class Persona(models.Model):
    nombre = models.CharField(max_length=30)
