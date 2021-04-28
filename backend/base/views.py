from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Person, Post
from .serializer import PersonSerializer, PostSerializer

@api_view(['GET'])
def getPeople(request):
    people = Person.objects.all()

    if 'name' in request.GET:
        name = request.GET['name']
        people = people.filter(name__icontains=name)
        
    people_serializer = PersonSerializer(people, many=True)
    
    return Response(people_serializer.data)

@api_view(['GET'])
def getPerson(request, pk):
    person = Person.objects.get(id=pk)

    print(request.GET)
    person_serializer = PersonSerializer(person)
    
    return Response(person_serializer.data)

@api_view(['GET'])
def getPosts(request):

    posts = Post.objects.all()
    post_serializer = PostSerializer(posts, many=True)

    return Response(post_serializer.data)

