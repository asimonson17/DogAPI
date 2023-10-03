from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from dogs.models import Dog, Breed
from dogs.serializers import DogSerializer, BreedSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

def index(request):
    return HttpResponse("Hello, world")
    
class DogViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing dog instances.
    """
    serializer_class = DogSerializer
    queryset = Dog.objects.all()
    
class BreedViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing dog instances.
    """
    serializer_class = BreedSerializer
    queryset = Breed.objects.all()

class DogList(APIView):
    """
    List all dogs, or create a new dog.
    """
    def get(self, request, format=None):
        dogs = Dog.objects.all()
        serializer = DogSerializer(dogs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class DogDetail(APIView):
    """
    Retrieve, update or delete a dog instance.
    """
    def get_object(self, pk):
        try:
            return Dog.objects.get(pk=pk)
        except Dog.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        dog = self.get_object(pk)
        serializer = DogSerializer(dog)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        dog = self.get_object(pk)
        serializer = DogSerializer(dog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        dog = self.get_object(pk)
        dog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
class BreedList(APIView):
    """
    List all breeds, or create a new breed.
    """
    def get(self, request, format=None):
        breeds = Breed.objects.all()
        serializer = BreedSerializer(breeds, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BreedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class BreedDetail(APIView):
    """
    Retrieve, update or delete a breed instance.
    """
    def get_object(self, pk):
        try:
            return Breed.objects.get(pk=pk)
        except Breed.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        breed = self.get_object(pk)
        serializer = BreedSerializer(breed)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        breed = self.get_object(pk)
        serializer = BreedSerializer(breed, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        breed = self.get_object(pk)
        breed.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)