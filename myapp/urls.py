from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import CharacterViewsSet

router = DefaultRouter()
router.register(r'characters', CharacterViewsSet, basename='character')

urlpatterns = [
    path('', include(router.urls)),
]