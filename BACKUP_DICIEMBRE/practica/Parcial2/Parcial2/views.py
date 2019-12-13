#from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def saludar(request,nombre):
    nombre = str(nombre)
    return HttpResponse("hola %s"%(nombre))
