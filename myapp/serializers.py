from rest_framework import serializers
from .models import Character

class CharacterSerializer(serializers.ModelSerializer):
    
    def validate_height(self, value):
        try:
            value = float(value)
        except ValueError:
            raise serializers.ValidationError("O valor deve ser um número.")
        
        if value < 0:
            raise serializers.ValidationError("A altura não pode ser negativa.")
        return value
    class Meta:
        model = Character
        fields = '__all__'
        extra_kwargs = {
            'name': {'help_text': 'Nome do personagem'},
            'height': {'help_text': 'Altura do personagem'},
            'mass': {'help_text': 'Massa do personagem'},
            'name': {'error_messages': {'blank': 'Nome é obrigatório.'}},
        }