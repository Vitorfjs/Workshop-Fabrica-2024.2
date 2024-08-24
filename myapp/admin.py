from django.contrib import admin
from .models import Character

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ('name', 'height', 'mass', 'gender')
    list_filter = ('gender', 'hair_color')
    search_fields = ('name', 'eye_color', 'birth_year')
    ordering = ('name',)