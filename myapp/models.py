from django.db import models

class Character(models.Model):
    name = models.CharField(max_length=100)
    height = models.CharField(max_length=10)
    mass = models.CharField(max_length=10)
    hair_color = models.CharField(max_length=20)
    skin_color = models.CharField(max_length=20)
    eye_color = models.CharField(max_length=20)
    birth_year = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    
    def __str__(self):
        return f'Nome: {self.name}'
