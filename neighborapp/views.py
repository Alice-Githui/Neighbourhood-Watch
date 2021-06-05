from django.shortcuts import render
from .serializers import *
from .models import  *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


# Create your views here.
class Registration(APIView):
        serializer_class=RegistrationSerializer

        def post(self, request):
            serializer=self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            user_data=serializer.data

            response={
                "data":{
                    "user":dict(user_data),
                    "status":"Success",
                    "message":"User account created successfully"
                }

            }
            return Response(response, status=status.HTTP_201_CREATED)

class NeighborhoodList(APIView):
    serializer_class=NeighbourhoodSerializer    
    # retrieve all objects in the neighbourhood model
    def get(self,request,format=None):
        neighborhood= Neighbourhood.objects.all()
        serializers=NeighbourhoodSerializer(neighborhood, many=True)
        return Response(serializers.data)

    # post an object to the neighbourhood model
    def post(self, request, format=None):
        serializers=self.serializer_class(data=request.data)
        if serializers.is_valid():
            serializers.save()
            neighbourhood=serializers.data

            response={
                "data":{
                    "new_hood":dict(neighbourhood),
                    "status":"Success",
                    "message":"New neighbourhood created successfully"
                }
            }
            return Response(response, status=status.HTTP_200_OK)
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

    # delete an existing neighbourhood
    def delete(self, request, pk, format=None):
        neighbour=self.get_neighbourhood(pk)
        neighbour.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BusinessList(APIView):
    serializer_class=BusinessSerializer
    # get all businesses from the database
    def get(self, request,format=None):
        business=Business.objects.all()
        serializers=BusinessSerializer(business, many=True)
        return Response(serializers.data)

    # post a new business to the database
    def post(self, request, format=None):
        serializers=self.serializer_class(data=request.data)
        if serializers.is_valid():
            serializers.save()
            business=serializers.data

            response={
                "data":{
                    "business":dict(business),
                    "status":"Success", 
                    "message":"New Business Created Successfully"
                }
            }
            return Response(response, status=status.HTTP_200_OK)
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

    # delete an existing business
    def delete(self, request, pk, format=None):
        business=self.get_business(pk)
        business.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserList(APIView):  
    serializer_class=ProfileSerializer
    # retrieve all users from the database
    def get(self,request,format=None):
        users=Profile.objects.all()
        serializers=ProfileSerializer(users, many=True)
        return Response(serializers.data)
    
    # post a new user to the database
    def post(self, request, format=None):
        serializers=self.serializer_class(data=request.data)
        if serializers.is_valid():
            serializers.save()
            user=serializers.data

            response={
                "data":{
                    "user":"user", 
                    "status":"Success", 
                    "message": "New User created successfully"
                }
            }
            return Response(response, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetails(APIView):
    # retrieve a single user from the database
    def get_user(self, pk):
        try:
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            return Http404
    
    def get(self, request, pk, format=None):
        users=self.get_user(pk)
        serializers=ProfileSerializer(users)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        user=self.get_user(pk)
        serializers=ProfileSerializer(user, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
  
    # delete an existing user
    def delete(self, request, pk, format=None):
        user=self.get_user(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

