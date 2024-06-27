# models.py
from django.db import models
from django.contrib.auth.models import User

class ProduccionDiaria(models.Model):
    estacion = models.CharField(max_length=100)
    fecha = models.DateField()
    gasolina = models.DecimalField(max_digits=10, decimal_places=2)
    diesel = models.DecimalField(max_digits=10, decimal_places=2)
    operador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='producciones')

    def __str__(self):
        return f"{self.estacion} - {self.fecha}"

