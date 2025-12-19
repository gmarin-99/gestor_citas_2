from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cita(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    descripcion = models.TextField()

    def __str__(self):
        return f"{self.usuario} - {self.fecha}"