from django.shortcuts import render
from .serializers import *
from .models import  *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class NeighborhoodList(APIView):    
    # retrieve all objects in the neighbourhood model
    def get(self,request,format=None):
        neighborhood= Neighbourhood.objects.all()
        serializers=NeighbourhoodSerializer(neighborhood, many=True)
        return Response(serializers.data)

    # post an object to the neighbourhood model
    def post(self, request, format=None):
        serializers=NeighbourhoodSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class NeighbourhoodDetails(APIView):
    # get a specific neighbourhood details
    def get_neighbourhood(self, pk):
        try:
            return Neighbourhood.objects.get(pk=pk)
        except Neighbourhood.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        neighbourhood=self.get_neighbourhood(pk)
        serializers=NeighbourhoodSerializer(neighbourhood)
        return Response(serializers.data)


class BusinessList(APIView):
    # get all businesses from the database
    def get(self, request,format=None):
        business=Business.objects.all()
        serializers=BusinessSerializers(business, many=True)
        return Response(serializers.data)

    # post a new business to the database
    def post(self, request, format=None):
        serializers=BusinessSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class BusinessDetails(APIView):
    # get one business from the database
    def get_business(self, pk):
        try:
            return Business.objects.get(pk=pk)
        except Business.DoesNotExist:
            return Http404
    
    def get(self,request, pk, format=None):
        business=self.get_business(pk)
        serializers=BusinessSerializers(business)
        return Response(serializers.data)

class UserList(APIView):  
    def get(self,request,format=None):
        users=User.objects.all()
        serializers=UserSerializer(users, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers=UserSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)