from rest_framework import serializers
from .models import ProduccionDiaria


class ProduccionDiariaSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProduccionDiaria
        fields='__all__' 
        #agregamos todos los campos para serealizar
