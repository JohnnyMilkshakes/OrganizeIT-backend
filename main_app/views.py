from django.shortcuts import render
from rest_framework import generics
from .models import Location
from .serializers import LocationSerializer

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