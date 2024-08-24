import requests
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Character
from .serializers import CharacterSerializer
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination

class CharacterPagination(PageNumberPagination):
    page_size = 10

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
    pagination_class = CharacterPagination

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