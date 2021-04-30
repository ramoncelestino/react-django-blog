from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Person, Post
from .serializer import PersonSerializer, PostSerializer
from rest_framework import status


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

@api_view(['GET', 'POST'])
def getPosts(request):
    if request.method == 'GET':
        posts = Post.objects.order_by('-created_data')
        post_serializer = PostSerializer(posts, many=True)

        return Response(post_serializer.data)
    
    elif request.method == 'POST':
        print(request.data)
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            print("AQUUI")
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getPost(request, pk):
    post = Post.objects.get(id=pk)

    serializer = PostSerializer(post)

    return Response(serializer.data)



    

        

