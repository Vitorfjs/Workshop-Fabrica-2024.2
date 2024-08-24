from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

class CharacterAPITestCase(TestCase):
    # Testes para a API de Personagens.
    
    def setUp(self):
        # Configura o cliente de teste e a URL base.
        
        self.client = APIClient() # Inicializa o cliente de API
        self.url = '/api/characters/' # Define a URL para os testes

    def test_list_characters(self):
        # Testa a listagem de personagens.
        
        response = self.client.get(self.url) # Faz uma requisição GET
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Verifica se o status é 200 OK