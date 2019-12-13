from django.db import models

Class Saludar(models.Model):
    saludo = models.TextField()
   
    def __str__(self):
        return self.saludo
