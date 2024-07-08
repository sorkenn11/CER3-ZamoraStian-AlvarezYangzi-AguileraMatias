# admin.py
from django.contrib import admin
from .models import ProduccionDiaria, Planta, Producto

admin.site.register(ProduccionDiaria)
admin.site.register(Planta)
admin.site.register(Producto)
