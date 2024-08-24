import requests
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Character
from .serializers import CharacterSerializer
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination


class CharacterPagination(PageNumberPagination):
    # Define a paginação para a listagem de personagens.
    page_size = 10 # Número de itens por página

class CharacterFilter(filters.FilterSet):
    # Define filtros para a busca de personagens.
    name = filters.CharFilter(lookup_expr='icontains') # Filtro por nome
    
    class Meta:
        model = Character # Modelo a ser filtrado
        fields = ['name'] # Campos disponíveis para filtragem

class CharacterViewSet(viewsets.ModelViewSet):
    # ViewSet para o modelo Character.
    
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer 
    filter_backends = (DjangoFilterBackend,) # Backend para filtros
    filterset_class = CharacterFilter # Classe de filtros
    pagination_class = CharacterPagination # Configuração de paginação

    def list(self, request):
        # Sincronizar dados da API externa com o banco de dados
        response = requests.get('https://swapi.dev/api/people/') # Faz uma requisição para a SWAPI
        data = response.json().get('results', []) # Obtém os resultados da resposta
        
        characters = [] # Lista para armazenar personagens
        
        for item in data:
            # Atualiza ou cria o personagem no banco de dados
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
            characters.append(character) # Adiciona o personagem à lista
        
        # Aplicar o filtro ao queryset
        queryset = self.filter_queryset(self.get_queryset())
        serializer = CharacterSerializer(queryset, many=True) # Serializa a lista de personagens
        return Response(serializer.data) # Retorna os dados serializados