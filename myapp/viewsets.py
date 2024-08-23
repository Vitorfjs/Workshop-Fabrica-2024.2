import requests
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Character
from .serializers import CharacterSerializer
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend

class CharacterFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = Character
        fields = ['name']

class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CharacterFilter

    def list(self, request):
        # Sincronizar dados da API externa com o banco de dados
        response = requests.get('https://swapi.dev/api/people/')
        data = response.json().get('results', [])
        
        characters = []
        
        for item in data:
            character, created = Character.objects.update_or_create(
                name=item['name'],
                defaults={
                    'height': item['height'],
                    'mass': item['mass'],
                    'hair_color': item['hair_color'],
                    'skin_color': item['skin_color'],
                    'eye_color': item['eye_color'],
                    'birth_year': item['birth_year'],
                    'gender': item['gender'],
                }
            )
            characters.append(character)
        
        serializer = CharacterSerializer(characters, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def create_character(self, request):
        # Criação de personagem não é necessário aqui, ModelViewSet já lida com isso
        return Response({'detail': 'Não permitido'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    @action(detail=True, methods=['put', 'patch'])
    def update_character(self, request, pk=None):
        # Atualização de personagem não é necessário aqui, ModelViewSet já lida com isso
        return Response({'detail': 'Não permitido'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    @action(detail=True, methods=['delete'])
    def delete_character(self, request, pk=None):
        # Exclusão de personagem não é necessário aqui, ModelViewSet já lida com isso
        return Response({'detail': 'Não permitido'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
