from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Person
from .serializer import PersonSerializer

@api_view(['GET'])
def getProducts(request):
    people = Person.objects.all()
    people_serializer = PersonSerializer(people, many=True)
    
    return Response(people_serializer.data)