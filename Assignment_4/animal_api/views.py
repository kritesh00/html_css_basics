from django.shortcuts import render
from rest_framework import generics
from .models import Animal
from .serializers import AnimalSerializer

# Create your views here.

class AnimalListCreateView(generics.ListCreateAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
class AnimalDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer