from django.shortcuts import render
from .models import Country
from rest_framework import generics
from .serializers import CountrySerializer

# Create your views here.

class CountryListView(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class CountryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer