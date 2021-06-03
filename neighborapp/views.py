from django.shortcuts import render
from .serializers import *
from .models import  *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class NeighborhoodList(APIView):
    def get(self,request,format=None):
        neighborhood= Neighbourhood.objects.all()
        serializers=NeighbourhoodSerializer(neighborhood, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers=NeighbourhoodSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class BusinessList(APIView):
    def get(self, request,format=None):
        business=Business.objects.all()
        serializers=BusinessSerializers(business, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers=BusinessSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

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