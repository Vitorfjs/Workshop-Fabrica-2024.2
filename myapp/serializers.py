from rest_framework import serializers
from .models import Character

class CharacterSerializer(serializers.ModelSerializer):
    # Serializador para o modelo Character.
    
    def validate_height(self, value):
        # Valida a altura como um número positivo.
        try:
            value = float(value) # Converte para float
        except ValueError:
            raise serializers.ValidationError("O valor deve ser um número.") # Erro se não for número
        
        if value < 0:
            raise serializers.ValidationError("A altura não pode ser negativa.") # Erro se negativo
        return value
    class Meta:
        # Configurações do serializador.
        
        model = Character # Modelo associado
        fields = '__all__' # Inclui todos os campos
        extra_kwargs = {
            'name': {'help_text': 'Nome do personagem'}, # Texto de ajuda para 'name'
            'height': {'help_text': 'Altura do personagem'}, # Texto de ajuda para 'height'
            'mass': {'help_text': 'Massa do personagem'}, # Texto de ajuda para 'mass'
            'name': {'error_messages': {'blank': 'Nome é obrigatório.'}},  # Erro se 'name' estiver vazio
        }