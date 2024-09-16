from django.shortcuts import render
from rest_framework import generics
from .models import Location, Item
from .serializers import LocationSerializer, ItemSerializer

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

# Define the home view
class Home(APIView):
  def get(self, request):
    content = {'message': 'Welcome to the organize-it api home route!'}
    return Response(content)
  
class LocationList(generics.ListCreateAPIView):
  queryset = Location.objects.all()
  serializer_class = LocationSerializer
  
class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Location.objects.all()
  serializer_class = LocationSerializer
  lookup_field = 'id'
  
class ItemListCreate(generics.ListCreateAPIView):
  serializer_class = ItemSerializer

  def get_queryset(self):
    location_id = self.kwargs['location_id']
    return Item.objects.filter(location_id=location_id)

  def perform_create(self, serializer):
    location_id = self.kwargs['location_id']
    location = Location.objects.get(id=location_id)
    serializer.save(location=location)
    
class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = ItemSerializer
  lookup_field = 'id'

  def get_queryset(self):
    location_id = self.kwargs['location_id']
    return Item.objects.filter(location_id=location_id)
