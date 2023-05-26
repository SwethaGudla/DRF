from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializers
from .models import Task
from rest_framework import status

# from django.http import JsonResponse
# Create your views here.
@api_view(['GET'])
def api_crud(request):
    return Response("API Base Point")

@api_view(['GET'])
def taskList(request):
    task = Task.objects.all()
    serializers = TaskSerializers(task, many=True)
    return Response(serializers.data)
@api_view(['GET'])
def taskDetails(request,pk):
    task = Task.objects.get(id=pk)
    serializers = TaskSerializers(task,many=False)
    return Response(serializers.data)

@api_view(['POST'])
def taskCreate(request):
    serializers = TaskSerializers(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data,status=status.HTTP_201_CREATED) 
    return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def taskUpdate(request,pk):
    task = Task.objects.get(id=pk)
    serializers = TaskSerializers(instance = task,data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data,status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def taskDelete(request,pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response("Item successfully deeleted..!")