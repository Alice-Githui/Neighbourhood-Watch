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

    # update an existing neighbourhood
    def put(self, request, pk, format=None):
        neighbourhood=self.get_neighbourhood(pk)
        serializers=NeighbourhoodSerializer(neighbourhood, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class BusinessList(APIView):
    # get all businesses from the database
    def get(self, request,format=None):
        business=Business.objects.all()
        serializers=BusinessSerializer(business, many=True)
        return Response(serializers.data)

    # post a new business to the database
    def post(self, request, format=None):
        serializers=BusinessSerializer(data=request.data)
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
        serializers=BusinessSerializer(business)
        return Response(serializers.data)

    # update a specific business 
    def put(self, request, pk, format=None):
        business=self.get_business(pk)
        serializers=BusinessSerializer(business, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class UserList(APIView):  
    # retrieve all users from the database
    def get(self,request,format=None):
        users=User.objects.all()
        serializers=UserSerializer(users, many=True)
        return Response(serializers.data)
    
    # post a new user to the database
    def post(self, request, format=None):
        serializers=UserSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetails(APIView):
    # retrieve a single user from the database
    def get_user(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Http404
    
    def get(self, request, pk, format=None):
        users=self.get_user(pk)
        serializers=UserSerializer(users)
        return Response(serializers.data)

