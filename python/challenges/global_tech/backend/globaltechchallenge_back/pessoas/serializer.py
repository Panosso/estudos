from rest_framework import serializers
from .models import Person

class PersonSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Person
        fields = [
            'id',
            'nome',
            'data_nascimento',
            'cpf',
            'sexo',
            'altura',
            'peso',
        ]

    def save(self, **kwargs):
        return super().save(**kwargs)
    
