from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from .serializers import *
from .models import *
from rest_framework import generics
from rest_framework import permissions
# Create your views here.
 

@api_view(['GET'])
def apioverview(request):
    api_urls={
        'List':'/task-list/',
        'Create':'/task-create/',
    }
    return Response(api_urls)


@api_view(['GET'])
def taskList(request):
    tasks=Task.objects.all()
    serializer=TaskSerializer(tasks,many=True)
    return Response(serializer.data)


@api_view(['POST'])
def taskCreate(request):
    
    serializer=TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def taskUpdate(request,pk):
    task=Task.objects.get(id=pk)
    serializer=TaskSerializer(instance=task,data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def taskDelete(request,pk):
    task=Task.objects.get(id=pk)
    task.delete()
    return Response('deleted')


class CarList(generics.ListCreateAPIView):
    serializer_class=CarSerializer
    queryset=Car.objects.all()


class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=CarSerializer
    queryset=Car