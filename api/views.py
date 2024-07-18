from django.shortcuts import render
from .models import Carlist
from rest_framework import viewsets
from .serilazers import CarlistSerializer
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


# Create your views here.
@api_view(['GET','POST'])
def CarlistList(request):
    if request.method == 'GET':
       carlist = Carlist.objects.all()
       serializer = CarlistSerializer(carlist, many=True)
       return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = CarlistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

@api_view(['GET','PUT','DELETE'])
def cardetail(request, pk):
    if request.method == 'GET':
        carlist = Carlist.objects.get(id=pk)
        serializer = CarlistSerializer(carlist)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        try:
            carlist = Carlist.objects.get(id=pk)
        except:
            return Response({'Not found data'},status=status.HTTP_404_NOT_FOUND)
        #carlist = Carlist.objects.get(id=pk)
        serializer = CarlistSerializer(carlist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
          return Response(serializer.errors)
        
    if request.method == 'DELETE':
        carlist = Carlist.objects.get(id=pk)
        carlist.delete()
       # return Response('deleted')
        return Response(status=status.HTTP_404_NOT_FOUND)




       
    



