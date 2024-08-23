import requests
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from .models import Character
from django.http import HttpResponse
from .serializers import CharacterSerializer

class CharacterViewsSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    
    def home(request):
        return HttpResponse("<h1>Bem vindo a Star Wars API</h1><p>Vá para <a href='/api/characters/'>Characters</a> para ver a lista de personagens.</p>")
    
    @action(detail=True, methods=['post'])
    def create_character(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=['put', 'patch'])
    def update_character(self, request, pk=None):
        character = self.get_object()
        serializer = self.get_serializer(character, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=['delete'])    
    def delete_character(self, request, pk=None):
        character = self.get_object()
        character.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def list(self, request):
        #listar personagens da Star Wars API
        response = requests.get('https://swapi.dev/api/people/')
        data = response.json()['results']
        
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