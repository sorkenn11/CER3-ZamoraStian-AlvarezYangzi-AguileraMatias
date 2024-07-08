# models.py
from django.db import models
from django.contrib.auth.models import User

class ProduccionDiaria(models.Model):
    estacion=models.CharField(max_length=100)
    turno=models.CharField(max_length=2) #AM PM MM
    fecha=models.DateField()
    hora=models.TimeField(default='00:00')
    litrosProduccion=models.DecimalField(max_digits=10, decimal_places=2)
    codigoPlanta=models.CharField(max_length=5, default='') #PRG, PRD, PRA
    codigoCombustible=models.CharField(max_length=5, default='') #G93, G95, G97, DIE, DIP, JA1, AVG
    operador=models.ForeignKey(User, on_delete=models.CASCADE, related_name='producciones')

    def __str__(self):
        return f"{self.estacion} - {self.fecha}"


class Planta(models.Model):
    nombrePlanta=models.CharField(max_length=100) 
    codigoPlanta=models.CharField(max_length=5) #PRG, PRD, PRA
    ubicacion=models.CharField(max_length=100) 

class Producto(models.Model):
    nombreProducto=models.CharField(max_length=100)
    codigoProducto=models.CharField(max_length=5) #G93, G95, G97, DIE, DIP, JA1, AVG 
    tipoProducto=models.CharField(max_length=100) #Gasolina, Diesel, Aviacion




